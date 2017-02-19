def printer(func):
    def wrapper(*args, **kwargs):
        print func.__name__, func
        return func(*args, **kwargs)
    return wrapper


@printer
def normal_func():
    pass


if __name__ == '__main__':
    normal_func()

