class MyMeta(type):
    pass
    def __new__(meta, name, bases, dict_):
        print '--> meta:', meta
        print '--> meta type:', type(meta)
        print '--> name:', name
        print '--> name type:', type(name)
        print '--> bases:', bases
        print '--> bases type:', type(bases)
        print '--> meta dict_:', dict_
        return super(MyMeta, meta).__new__(meta, name, bases, dict_)

class Klass():
    pass
    stuff = 1

class KlassObj(object):
    pass
    __metaclass__ = MyMeta
    stuff = 1




if __name__ == '__main__':
    c = Klass()
    cobj = KlassObj()
    print 'type c:'.ljust(25, '.'), type(c)
    print 'type cobj:'.ljust(25, '.'), type(cobj)

    print 'c:'.ljust(25, '.'), c
    print 'cobj:'.ljust(25, '.'), cobj

    print 'dir c:'.ljust(25, '.'), dir(c)
    print 'dir cobj:'.ljust(25, '.'), dir(cobj)

    print 'dir c.__class__:'.ljust(25, '.'), c.__class__
    print 'dir cobj.__class__:'.ljust(25, '.'), cobj.__class__

    print 'dir c.__module__:'.ljust(25, '.'), c.__module__
    print 'dir cobj.__module__:'.ljust(25, '.'), cobj.__module__

    print 'dir c.__dict__:'.ljust(25, '.'), c.__dict__
    print 'dir cobj.__dict__:'.ljust(25, '.'), cobj.__dict__

    # print 'dir c.__sizeof__:'.ljust(25, '.'), c.__sizeof__
    print 'dir cobj.__sizeof__():'.ljust(25, '.'), cobj.__sizeof__()

    print
    print '--> klassobj stuff:', KlassObj.stuff
    print '--> klassobj stuff:', type(KlassObj.stuff)
