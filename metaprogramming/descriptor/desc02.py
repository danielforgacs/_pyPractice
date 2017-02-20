class Descriptor(object):
    def __init__(self):
        self.value = 0

    def __get__(self, instance, cls):
        # return self.value
        getattr(instance, 'attr')

    def __set__(self, instance, value):
        setattr(instance, 'attr', value)
        # self.value = value

    def __delete__(self, instance):
        pass


class Strange(object):
    attr = Descriptor()
    # attr = None

    # def __init__(self):
    #     self.attr = None



s = Strange()
x = Strange()
print(s.attr)
print(x.attr)
x.attr = 3
print(s.attr)
print(x.attr)
# x.attr = -1
# print(s.attr)
# print(x.attr)
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