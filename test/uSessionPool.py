"""Module for testing session pools."""

import threading

class TestConnection(TestCase):

    def __ConnectAndDrop(self):
        """Connect to the database, perform a query and drop the connection."""
        connection = self.pool.acquire()
        cursor = connection.cursor()
        cursor.execute(u"select count(*) from TestNumbers")
        count, = cursor.fetchone()
        self.assertEqual(count, 10)

    def testPool(self):
        """test that the pool is created and has the right attributes"""
        pool = cx_Oracle.SessionPool(USERNAME, PASSWORD, TNSENTRY, 2, 8, 3)
        self.assertEqual(pool.username, USERNAME, "user name differs")
        self.assertEqual(pool.tnsentry, TNSENTRY, "tnsentry differs")
        self.assertEqual(pool.max, 8, "max differs")
        self.assertEqual(pool.min, 2, "min differs")
        self.assertEqual(pool.increment, 3, "increment differs")
        self.assertEqual(pool.opened, 2, "opened differs")
        self.assertEqual(pool.busy, 0, "busy not 0 at start")
        connection_1 = pool.acquire()
        self.assertEqual(pool.busy, 1, "busy not 1 after acquire")
        self.assertEqual(pool.opened, 2, "opened not unchanged (1)")
        connection_2 = pool.acquire()
        self.assertEqual(pool.busy, 2, "busy not 2 after acquire")
        self.assertEqual(pool.opened, 2, "opened not unchanged (2)")
        connection_3 = pool.acquire()
        self.assertEqual(pool.busy, 3, "busy not 3 after acquire")
        self.assertEqual(pool.opened, 5, "opened not changed (3)")
        pool.release(connection_3)
        self.assertEqual(pool.busy, 2, "busy not 2 after release")
        del connection_2
        self.assertEqual(pool.busy, 1, "busy not 1 after del")

    def testProxyAuth(self):
        """test that proxy authentication is possible"""
        pool = cx_Oracle.SessionPool(USERNAME, PASSWORD, TNSENTRY, 2, 8, 3)
        self.assertEqual(pool.homogeneous, 1,
                "homogeneous should be 1 by default")
        self.assertRaises(cx_Oracle.ProgrammingError, pool.acquire,
                user = "proxyuser")
        pool = cx_Oracle.SessionPool(USERNAME, PASSWORD, TNSENTRY, 2, 8, 3,
                homogeneous = False)
        self.assertEqual(pool.homogeneous, 0,
                "homogeneous should be 0 after setting it in the constructor")
        user = u"%s_proxy" % USERNAME
        connection = pool.acquire(user = user)
        cursor = connection.cursor()
        cursor.execute(u'select user from dual')
        result, = cursor.fetchone()
        self.assertEqual(result, user.upper())

    def testRollbackOnDel(self):
        "connection rolls back before being destroyed"
        pool = cx_Oracle.SessionPool(USERNAME, PASSWORD, TNSENTRY, 1, 8, 3)
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.execute(u"truncate table TestExecuteMany")
        cursor.execute(u"insert into TestExecuteMany (IntCol) values (1)")
        pool = cx_Oracle.SessionPool(USERNAME, PASSWORD, TNSENTRY, 1, 8, 3)
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.execute(u"select count(*) from TestExecuteMany")
        count, = cursor.fetchone()
        self.assertEqual(count, 0)

    def testRollbackOnRelease(self):
        "connection rolls back before released back to the pool"
        pool = cx_Oracle.SessionPool(USERNAME, PASSWORD, TNSENTRY, 1, 8, 3)
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.execute(u"truncate table TestExecuteMany")
        cursor.execute(u"insert into TestExecuteMany (IntCol) values (1)")
        pool.release(connection)
        pool = cx_Oracle.SessionPool(USERNAME, PASSWORD, TNSENTRY, 1, 8, 3)
        connection = pool.acquire()
        cursor = connection.cursor()
        cursor.execute(u"select count(*) from TestExecuteMany")
        count, = cursor.fetchone()
        self.assertEqual(count, 0)

    def testThreading(self):
        """test session pool to database with multiple threads"""
        self.pool = cx_Oracle.SessionPool(USERNAME, PASSWORD, TNSENTRY, 5, 20,
                2, threaded = True)
        threads = []
        for i in range(20):
            thread = threading.Thread(None, self.__ConnectAndDrop)
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

