import cx_Oracle

connection = cx_Oracle.connect(dsn=None, password=None, threaded=True, twophase=True, user='/')

print('connected with /')
