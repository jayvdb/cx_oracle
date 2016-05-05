from sqlalchemy.engine import create_engine

urls = [
    'oracle:///',
    'oracle:///@XE',
    'oracle://XE',
    'oracle:///@localhost/XE',
]

for url in urls:
    try:
        engine = create_engine(sqlalchemy_connect_url)
        connection = engine.connect()
        print('connected using %s' % url)
    except Exception as e:
        print('\nconnection as %s failed: %s' % (url, e))
