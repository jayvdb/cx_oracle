import cx_Oracle

connection = cx_Oracle.connect(dsn='/', password=None, threaded=True, twophase=True, user=None)

print('connected with /')
