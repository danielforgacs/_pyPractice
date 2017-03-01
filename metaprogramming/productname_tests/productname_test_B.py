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

class NameDescriptor(object):
    def __get__(self, instance, cls):
        pass
        if not instance.__dict__['bad']:
            name = '_'.join([
                instance.__dict__['region'],
                instance.__dict__['year'],
            ])
            return name

    def __set__(self, instance, value):
        raise AttributeError('===> NAME IS READ ONLY!')

class BadContainer(object):
    def __init__(self):
        self.bad = set()

class Region(Descriptor):
    opts = ('usa', 'ger')

class Year(Descriptor):
    opts = ('15', '16', '17')

class VarName(BadContainer):
    region = Region(name='region')
    year = Year(name='year')
    name = NameDescriptor()

    def __init__(self, name=None, year=None):
        super().__init__()
        elements = [elem for elem in type(self).__dict__.keys()
                    if not elem.startswith('__')]
        for elem in elements:
            if elem != 'name':
                setattr(self, elem, None)

    # @property
    # def name(self):
    #     pass

variant = VarName()
# variant_b = VarName()
print(variant.__dict__)
variant.region = 'usa'
# variant.name = 'd'
print(variant.__dict__)
print(variant.name)
print(bool(variant.name))
print(variant.bad)
variant.year = '15'
print(variant.name)
print(bool(variant.name))
print(variant.bad)



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