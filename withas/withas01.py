class WA(object):
    def __enter__(self):
        print('--> ENTER...')


    def __exit__(self, exc_type, exc_value, traceback):
        print('--> EXIT...')


with WA() as k:
    print('--> inside...')
    raise Exception('no worries, exit run!')