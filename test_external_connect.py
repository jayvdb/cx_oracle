import cx_Oracle

try:
    connection = cx_Oracle.connect(user='/')
    print('connected with user=/ ')
except Exception as e:
    print('\nconnection using user=/ failed: %s' % e)

try:
    connection = cx_Oracle.connect(user='/', dsn=None)
    print('connected with user=/ , dsn=None')
except Exception as e:
    print('\nconnection using user=/ dsn=None failed: %s' % e)

try:
    pool = cx_Oracle.SessionPool(user='',password='',dsn='XE',min=1,max=2,increment=1,externalauth=True)
    connection = pool.acquire()
    print('pool connected using externalauth=True')
except Exception as e:
    print('\npool connection using externalauth=True failed: %s' % e)

try:
    pool = cx_Oracle.SessionPool(user=None,password=None,dsn=None,min=1,max=2,increment=1,externalauth=True)
    connection = pool.acquire()
    print('pool connected using externalauth=True with None')
except Exception as e:
    print('\npool connection using externalauth=True with None failed: %s' % e)

try:
    pool = cx_Oracle.SessionPool(user='/',password=None,dsn=None,min=1,max=2,increment=1,externalauth=True)
    connection = pool.acquire()
    print('pool connected using externalauth=True with None')
except Exception as e:
    print('\npool connection using externalauth=True with None failed: %s' % e)

try:
    connection = cx_Oracle.connect('/', mode=cx_Oracle.SYSDBA)
    print('connected with / as sysdba')
except Exception as e:
    print('\nconnection using / as sysdba failed: %s' % e)

try:
    connection = cx_Oracle.connect(dsn='/', mode=cx_Oracle.SYSDBA)
    print('connected with dsn=/ as sysdba')
except Exception as e:
    print('\nconnection using dsn=/ as sysdba failed: %s' % e)

try:
    connection = cx_Oracle.connect(user='/', mode=cx_Oracle.SYSDBA)
    print('connected with user=/ as sysdba')
except Exception as e:
    print('\nconnection using user=/ as sysdba failed: %s' % e)

try:
    connection = cx_Oracle.connect(dsn='XE', password=None, user=None)
    print('connected with dsn=XE')
except Exception as e:
    print('\nconnection using just dsn failed: %s' % e)

try:
    connection = cx_Oracle.connect(dsn='XE', password=None, user='/')
    print('connected with dsn=XE user = /')
except Exception as e:
    print('\nconnection using just dsn and user / failed: %s' % e)

try:
    connection = cx_Oracle.connect(dsn='XE', password='', user='/')
    print('connected with dsn=XE user = /  password =')
except Exception as e:
    print('\nconnection using dsn and user / and empty password failed: %s' % e)

cargs = tuple()
kwargs = {'user': '/'}

try:
    connection = cx_Oracle.connect(*cargs, **kwargs)
    print('connected with %r' % kwargs)
except Exception as e:
    print('\nconnection with %r failed: %s' % (kwargs, e))

kwargs = {'user': '/', 'dsn': None}

try:
    connection = cx_Oracle.connect(*cargs, **kwargs)
    print('connected with %r' % kwargs)
except Exception as e:
    print('\nconnection with %r failed: %s' % (kwargs, e))

kwargs = {'dsn': None, 'user': '/'}

try:
    connection = cx_Oracle.connect(*cargs, **kwargs)
    print('connected with %r' % kwargs)
except Exception as e:
    print('\nconnection with %r failed: %s' % (kwargs, e))

kwargs = {'dsn': None, 'password': None, 'user': '/'}

try:
    connection = cx_Oracle.connect(*cargs, **kwargs)
    print('connected with %r' % kwargs)
except Exception as e:
    print('\nconnection with %r failed: %s' % (kwargs, e))

kwargs['password'] = ''

try:
    connection = cx_Oracle.connect(*cargs, **kwargs)
    print('connected with %r' % kwargs)
except Exception as e:
    print('\nconnection with %r failed: %s' % (kwargs, e))
