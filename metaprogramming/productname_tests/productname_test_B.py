class Descriptor(object):
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        # print(instance.__dict__)
        instance.__dict__[self.name] = value


class Opted(Descriptor):
    def __set__(self, instance, value):
        if value not in self.opts:
            pass
            # raise ValueError('===> NOT IN OPTIONS.')
            # instance.__dict__['bad'].add(value)

        super().__set__(instance, value)

class Region(Opted):
    opts = ('usa', 'ger')

class NameBase(type):
    # bad = None
    def __new__(cls, name, bases, dict_):
        dict_.update({'bad': None})
        # print(dict_)
        return type(name, bases, dict_)

# class VarName(object):
class VarName(metaclass=NameBase):
    region = Region(name='region')
    # year =



variant = VarName()
variant_b = VarName()
# print(VarName.__dict__)
# print(variant.__dict__)
# print(variant.__dict__)
# variant.region = 'usa'
# print(variant.__dict__)
variant.region = 'ger'
variant_b.region = 'usa'
variant_b.region = 'x'
# variant_b.bad = 999
# print(variant.region)
print(variant.__dict__)
# print(variant.bad)
# print(variant_b.region)
print(variant_b.__dict__)
# print(variant_b.bad)