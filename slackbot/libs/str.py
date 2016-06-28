def str_encode(string):
    if isinstance(string, str):
        return string.decode('utf-8')
    elif isinstance(string, unicode):
        return string.encode('utf-8')
    else:
        print 'unsupport type {}'.format(type(string))
