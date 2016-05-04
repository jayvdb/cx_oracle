import cx_Oracle

connection = cx_Oracle.connect("", "", "/")

print('connected')

connection = cx_Oracle.connect(None, None, "/")

print('connected 2')
