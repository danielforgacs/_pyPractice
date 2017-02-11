import re

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def camel_to_snake_case(name, bases, attrs):
    print('Calling the metaclass'
        'camel_to_snake_case to construct class: {}'.format(name))

    snake_attrs = {}

    for attr_name, attr_val in attrs.items():
        if not name.startswith('__'):
            snake_attrs[convert(attr_name)] = attr_val

        else:
            snake_attrs[attr_name] = attr_val

    return type(name, bases, snake_attrs)


class MyVector(object):
    __metaclass__ = camel_to_snake_case

    def addToVector(self, other):
        pass

    def subtractFromVector(self, other):
        pass

    def calculateDotProduct(self, other):
        pass

    def calculateCrossProduct(self, other):
        pass

    def calculateTripleProduct(self, other):
        pass

    def someOtherMethod(self):
        pass

    def longMethNameWLotOfUpperCase(self):
        pass


print([a for a in dir(MyVector) if not a.startswith('__')])