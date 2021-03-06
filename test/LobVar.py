"""Module for testing LOB (CLOB and BLOB) variables."""

import sys

class TestLobVar(BaseTestCase):

    def __PerformTest(self, type, inputType):
        longString = ""
        directType = getattr(cx_Oracle, type)
        self.cursor.execute("truncate table Test%ss" % type)
        for i in range(0, 11):
            if i > 0:
                char = chr(ord('A') + i - 1)
                longString += char * 25000
            elif inputType != directType:
                continue
            self.cursor.setinputsizes(longString = inputType)
            if type == "BLOB" and sys.version_info[0] >= 3:
                bindValue = longString.encode("ascii")
            else:
                bindValue = longString
            self.cursor.execute("""
                    insert into Test%ss (
                      IntCol,
                      %sCol
                    ) values (
                      :integerValue,
                      :longString
                    )""" % (type, type),
                    integerValue = i,
                    longString = bindValue)
        self.connection.commit()
        self.cursor.execute("""
                select *
                from Test%ss
                order by IntCol""" % type)
        longString = ""
        for row in self.cursor:
            integerValue, lob = row
            if integerValue == 0:
                self.assertEqual(lob.size(), 0)
                expectedValue = ""
                if type == "BLOB" and sys.version_info[0] >= 3:
                    expectedValue = expectedValue.encode("ascii")
                self.assertEqual(lob.read(), expectedValue)
            else:
                char = chr(ord('A') + integerValue - 1)
                prevChar = chr(ord('A') + integerValue - 2)
                longString += char * 25000
                if type == "BLOB" and sys.version_info[0] >= 3:
                    actualValue = longString.encode("ascii")
                    char = char.encode("ascii")
                    prevChar = prevChar.encode("ascii")
                else:
                    actualValue = longString
                self.assertEqual(lob.size(), len(actualValue))
                self.assertEqual(lob.read(), actualValue)
                if type == "CLOB":
                    self.assertEqual(str(lob), actualValue)
                self.assertEqual(lob.read(len(actualValue)), char)
            if integerValue > 1:
                offset = (integerValue - 1) * 25000 - 4
                string = prevChar * 5 + char * 5
                self.assertEqual(lob.read(offset, 10), string)

    def __TestTrim(self, type):
        self.cursor.execute("truncate table Test%ss" % type)
        self.cursor.setinputsizes(longString = getattr(cx_Oracle, type))
        longString = "X" * 75000
        if type == "BLOB" and sys.version_info[0] >= 3:
            longString = longString.encode("ascii")
        self.cursor.execute("""
                insert into Test%ss (
                  IntCol,
                  %sCol
                ) values (
                  :integerValue,
                  :longString
                )""" % (type, type),
                integerValue = 1,
                longString = longString)
        self.cursor.execute("""
                select %sCol
                from Test%ss
                where IntCol = 1""" % (type, type))
        lob, = self.cursor.fetchone()
        self.assertEqual(lob.size(), 75000)
        lob.trim(25000)
        self.assertEqual(lob.size(), 25000)
        lob.trim()
        self.assertEqual(lob.size(), 0)

    def testBLOBCursorDescription(self):
        "test cursor description is accurate for BLOBs"
        self.cursor.execute("select * from TestBLOBs")
        self.assertEqual(self.cursor.description,
                [ ('INTCOL', cx_Oracle.NUMBER, 10, 22, 9, 0, 0),
                  ('BLOBCOL', cx_Oracle.BLOB, -1, 4000, 0, 0, 0) ])

    def testBLOBsDirect(self):
        "test binding and fetching BLOB data (directly)"
        self.__PerformTest("BLOB", cx_Oracle.BLOB)

    def testBLOBsIndirect(self):
        "test binding and fetching BLOB data (indirectly)"
        self.__PerformTest("BLOB", cx_Oracle.LONG_BINARY)

    def testBLOBTrim(self):
        "test trimming a BLOB"
        self.__TestTrim("BLOB")

    def testCLOBCursorDescription(self):
        "test cursor description is accurate for CLOBs"
        self.cursor.execute("select * from TestCLOBs")
        self.assertEqual(self.cursor.description,
                [ ('INTCOL', cx_Oracle.NUMBER, 10, 22, 9, 0, 0),
                  ('CLOBCOL', cx_Oracle.CLOB, -1, 4000, 0, 0, 0) ])

    def testCLOBsDirect(self):
        "test binding and fetching CLOB data (directly)"
        self.__PerformTest("CLOB", cx_Oracle.CLOB)

    def testCLOBsIndirect(self):
        "test binding and fetching CLOB data (indirectly)"
        self.__PerformTest("CLOB", cx_Oracle.LONG_STRING)

    def testCLOBTrim(self):
        "test trimming a CLOB"
        self.__TestTrim("CLOB")

    def testMultipleFetch(self):
        "test retrieving data from a CLOB after multiple fetches"
        self.cursor.arraysize = 1
        self.cursor.execute("select CLOBCol from TestCLOBS")
        rows = self.cursor.fetchall()
        self.assertRaises(cx_Oracle.ProgrammingError, rows[1][0].read)

    def testNCLOBCursorDescription(self):
        "test cursor description is accurate for NCLOBs"
        self.cursor.execute("select * from TestNCLOBs")
        self.assertEqual(self.cursor.description,
                [ ('INTCOL', cx_Oracle.NUMBER, 10, 22, 9, 0, 0),
                  ('NCLOBCOL', cx_Oracle.NCLOB, -1, 4000, 0, 0, 0) ])

    def testNCLOBsDirect(self):
        "test binding and fetching NCLOB data (directly)"
        self.__PerformTest("NCLOB", cx_Oracle.NCLOB)

    def testNCLOBsIndirect(self):
        "test binding and fetching NCLOB data (indirectly)"
        self.__PerformTest("NCLOB", cx_Oracle.LONG_STRING)

    def testNCLOBTrim(self):
        "test trimming a CLOB"
        self.__TestTrim("CLOB")

