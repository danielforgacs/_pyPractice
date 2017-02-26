class Descriptor(object):
    def __init__(self, attrname='n/a'):
        self.attrname = attrname

    def __get__(self, instance, cls):
        return instance.__dict__.get(self.attrname)

    def __set__(self, instance, value):
        instance.__dict__[self.attrname] = value

class Typed(Descriptor):
    def __set__(self, instance, value):
        if not isinstance(value, self.attrtype):
            raise TypeError('==> MUST BE TYPE '+str(self.attrtype))
        super().__set__(instance, value)

class StringTyped(Typed):
    attrtype = str

class SizedString(Descriptor):
    def __init__(self, maxlen=3, *args, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if len(value) > self.maxlen:
            raise AttributeError('==> TOO LONG.')
        super().__set__(instance, value)

class Name(StringTyped, SizedString):
    pass

class ProductName(object):
    pass
    name = Name(attrname='name')
    # year = Year(attrname='year')

if __name__ == '__main__':
    p = ProductName()
    # print(p.__dict__)
    p.name = '1'
    print(p.__dict__)
    # p.name = 1
    # print(p.__dict__)
    # print(p.name)
    # # print(p.name)
    # # p.name = 'aaaaaaaaaaa'
    # # print(p.__dict__)
    # # print(p.name)
    # p.year = 1
    # # p.year = -1
    # print(p.__dict__)
    # # p.year = '5'
    # print(p.__dict__)