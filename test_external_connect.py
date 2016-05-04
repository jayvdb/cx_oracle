import cx_Oracle

connection = cx_Oracle.connect(None, None, "/")

print('connected with None')

connection = cx_Oracle.connect("", "", "/")

print('connected')
