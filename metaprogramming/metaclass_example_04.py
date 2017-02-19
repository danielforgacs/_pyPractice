import re

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def camel_to_snake_case(name, bases, attrs):
    # print attrs

    snake_attrs = {}

    for attr_name, attr_val in attrs.items():
        if not name.startswith('__'):
            snake_attrs[convert(attr_name)] = attr_val

        else:
            snake_attrs[attr_name] = attr_val

    return type(name, bases, snake_attrs)


class MyVector(object):
    def calculateTripleProduct(self, other):
        pass

    def someOtherMethod(self):
        pass

    def longMethNameWLotOfUpperCase(self):
        pass


class NewVector(MyVector):
    print dir()
    __metaclass__ = camel_to_snake_case
    print dir()
    pass


# print([a for a in dir(NewVector) if not a.startswith('__')])