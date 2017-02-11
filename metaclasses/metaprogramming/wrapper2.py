from functools import wraps


def printer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print func.__name__, func
        return func(*args, **kwargs)
    return wrapper


@printer
def normal_func():
    """
    blskjd ksfdv hjdfvg
    """
    pass


if __name__ == '__main__':
    normal_func()
    print (help(normal_func))

