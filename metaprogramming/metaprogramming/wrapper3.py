import time
import datetime
from functools import wraps


def printer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print func.__name__, func
        t0 = datetime.datetime.now()
        result = func(*args, **kwargs)
        print 'elapsed time:', datetime.datetime.now() - t0
        return result
    return wrapper


class A(object):
    @printer
    def a_method(self):
        pass
        time.sleep(1)


@printer
def normal_func():
    """
    blskjd ksfdv hjdfvg
    """
    time.sleep(1)
    pass


if __name__ == '__main__':
    normal_func()
    print (help(normal_func))

    a = A()
    a.a_method()