class OrderedDescriptor(object):
    def __init__(self, attrname):
        self.attrname = attrname
        self.isorderset = False

    def __get__(self, instance, cls):
        return instance.__dict__[self.attrname]

    def __set__(self, instance, value):
        if not self.isorderset:
            instance.__dict__['order'].append(self.attrname)
        instance.__dict__[self.attrname] = value

class VN(object):
    region = OrderedDescriptor(attrname='region')
    year = OrderedDescriptor(attrname='year')
    extra = OrderedDescriptor(attrname='extra')

    def __init__(self, k=1):
        self.order = []
        # self.region = 'region'
        # self.year = 'year'
        # self.extra = 'extra'

    def pr(self):
        print self.__dict__.keys()
        print '_'.join([self.__dict__[k] for k in self.order])

vn = VN()
# print vn.__dict__
vn.pr()
vn.region = 'region'
vn.year = 'year'
vn.extra = 'extra'
vn.pr()
print vn.region
print vn.year
print vn.extra
