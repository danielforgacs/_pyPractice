import err
import m1
import m2
import m3

try:
    import mx
except ImportError as error:
    print('!ERROR:', error)
    mx = None


def func_main():
    pass



def main():
    print('main.func_main')
    func_main()
    m1.func_m1()
    m2.func_m2()


if __name__ == '__main__':
    pass
    main()
