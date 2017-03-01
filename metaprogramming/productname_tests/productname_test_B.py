class Descriptor(object):
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value not in self.opts:
            instance.__dict__['bad'] = instance.__dict__['bad'] | {self.name}
        else:
            instance.__dict__['bad'] = instance.__dict__['bad'] - {self.name}
        instance.__dict__[self.name] = value

class BadContainer(object):
    def __init__(self):
        # print(self.__dict__)
        self.bad = set()

class Region(Descriptor):
    opts = ('usa', 'ger')

class Year(Descriptor):
    opts = ('15', '16', '17')

class VarName(BadContainer):
    region = Region(name='region')
    year = Year(name='year')

    def __init__(self, name=None, year=None):
        super().__init__()
        self.region = name
        self.year = year

variant = VarName()
variant_b = VarName()
print(variant.__dict__)
# print(VarName.__dict__)
# print(VarName.__dict__)
# print(variant.__dict__)
# print(variant.__dict__)
# variant.region = 'usa'
# print(variant.__dict__)
# variant.region = 'ger'
# variant_b.region = 'usa'
# print(variant.__dict__)
# print(variant_b.__dict__)
# # variant_b.region = 'x'
# # variant_b.bad = 999
# # print(variant.region)
# # variant.region = 'ger'
# # print(variant.bad)
# # print(variant_b.region)
# # print(variant_b.bad)
# variant_b.region = 'x'
# print(variant_b.__dict__)
# variant_b.region = 'usa'
# print(variant_b.__dict__)
#
# variant_b.year = 'x'
# print(variant.__dict__)
# print(variant_b.__dict__)
# variant_b.region = 'usa'
# print(variant.__dict__)
# print(variant_b.__dict__)
#
# variant_b.year = '17'
# print(variant.__dict__)
# print(variant_b.__dict__)
# variant_b.region = 'd'
# print(variant.__dict__)
# print(variant_b.__dict__)
#