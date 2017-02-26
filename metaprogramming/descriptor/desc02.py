class Descriptor(object):
    # def __init__(self, *args, **kwargs):
    #     print(args)
    #     print(kwargs)
    #     self.value = 0
    #     # instance.__dict__['k'] = None

    def __get__(self, instance, cls):
        # return self.value
        # getattr(instance, 'attr')
        return instance.__dict__.get('k')

    def __set__(self, instance, value):
        # setattr(instance, 'attr', value)
        # self.value = value
        instance.__dict__['k'] = value

    def __delete__(self, instance):
        # raise Exception
        pass
        del instance.__dict__['k']


class Strange(object):
    attr = Descriptor()
    # attr = None

    def __init__(self):
        self.attr = 'stuff'



s = Strange()
x = Strange()
print(s.attr)
print(x.attr)
x.attr = 3
print(s.attr)
print(x.attr)
print(type(x.attr))
x.attr = -1
print(s.attr)
print(x.attr)
print(x.__dict__)
del x.attr
print(x.__dict__)
# s.attr = 'k'
# print(s.attr)
# print(x.attr)
# # print(Strange)
# # print(Strange.__dict__['attr'].__dict__)
# print(Strange.__dict__['attr'].__get__(x, Strange))
# # print(s)
# # print(s.attr)
# # print(type(s))
# # print(type(s).__dict__)
# # print(type(s).__dict__['attr'])
# # print(type(s).__dict__['attr'].__get__(s, type(s)))
# # print(Strange.__dict__['attr'].__get__(s, Strange))#