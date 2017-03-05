class Attrname(object):
    def __init__(self, attrname):
        self.attrname = attrname



class Descriptor(Attrname):
    def __get__(self, instance, cls):
        return instance.__dict__[self.attrname]

    def __set__(self, instance, value):
        instance.__dict__[self.attrname] = value



class TypedDescriptor(Descriptor):
    def __set__(self, instance, value):
        if not isinstance(value, self.valuetype):
            raise TypeError('===> MUST BE TYPE: '+str(self.valuetype))
        super(TypedDescriptor, self).__set__(instance, value)



class OptedDescriptor(Descriptor):
    def __set__(self, instance, value):
        if not value in self.options:
            raise ValueError('===> ALLOWED VALUES: '+str(self.options))
        super(OptedDescriptor, self).__set__(instance, value)



class StringTyped(TypedDescriptor):
    valuetype = str



class IntTyped(TypedDescriptor):
    valuetype = int



class Region(StringTyped, OptedDescriptor):
    options = ('fna', 'ger')



class ModelYear(IntTyped):
    year_min = 2000
    year_max = 2020

    def __set__(self, instance, value):
        if not (self.year_min <= value <= self.year_max):
            raise ValueError('===> MUST BE IN RANGE'
                    ': {} - {}'.format(str(self.year_min), str(self.year_max)))
        super(ModelYear, self).__set__(instance, value)



class VariantName(object):
    region = Region(attrname='region')
    year = ModelYear(attrname='year')

    def __init__(self, name=None):
        self._name = name

    @property
    def name(self):
        return self._name



if __name__ == '__main__':
    # variant = VariantName()
    pass
    # print variant.name
    # variant.region = 'fna'
    # variant.year = 2001
    # print variant.__dict__.keys()
    # print type(variant.__dict__['year'])
