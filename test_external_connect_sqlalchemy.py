from sqlalchemy.engine import create_engine, url

urls = [
    'oracle://',
    'oracle:///',
    'oracle:///@XE',
    'oracle:///:@XE',
    'oracle:///:@localhost/XE',
    'oracle://localhost/XE',
    'oracle://:@localhost/XE',
    'oracle://XE',
    'oracle://:@XE',
    'oracle://@',
    'oracle://@/',
    'oracle://:@',
    'oracle://:@/',
    'oracle:///@localhost/XE',
    'oracle://%2F',
    'oracle://%2F@',
    # 'oracle://%2F:',  # invalid literal for int() with base 10
    # 'oracle://%2F:/',  # invalid literal for int() with base 10
    'oracle://%2F:@',
    'oracle://%2F@XE',
    'oracle://%2F@localhost/XE',
]

for connect_url in urls:
    print('---')
    try:
        engine = create_engine(connect_url)
        u = url.make_url(connect_url)
        print('\n\nurl = %s' % connect_url)
        print('args = %r \nkwargs = %r' % engine.dialect.create_connect_args(u))
    except Exception as e:
        print('\nconnection args for %s failed: %s' % (connect_url, e))
    try:
        connection = engine.connect()
        print('connected using %s' % connect_url)
    except Exception as e:
        print('\nconnection as %s failed: %s' % (connect_url, e))
    print('---')


engine = create_engine('oracle://%2F@')
connection = engine.connect()