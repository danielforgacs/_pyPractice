class Descriptor(object):
    def __init__(self):
        pass

    def __get__(self, instance, cls):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass


class Strange(object):
    attr = Descriptor()



s = Strange()