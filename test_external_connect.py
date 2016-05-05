import cx_Oracle

try:
    connection = cx_Oracle.connect(dsn='XE', password=None, threaded=True, twophase=True, user=None)
    print('connected with dsn=XE')
except Exception as e:
    print(e)

try:
    connection = cx_Oracle.connect(dsn='XE', password=None, threaded=True, twophase=True, user='/')
    print('connected with dsn=XE user = /')
except Exception as e:
    print(e)



