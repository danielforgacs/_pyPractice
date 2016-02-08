class BadClass(object):
    def __init__(self):
        self.parms = {'focal': 1}

    def getAttr(self, attr):
        return self.parms[attr]

    def setAttr(self, attr, value):
        self.parms[attr] = value

        return self.parms[attr]


class BadClassWrapper(object):
    def __init__(self):
        self._focal = 35
        self.cam = BadClass()
        self.cam.setAttr('focal', 35)

    @property
    def focal(self):
        return self._focal

    @focal.setter
    def focal(self, value):
        self._focal = value
        self.cam.setAttr('focal', value)


class NewWrapper(object):
    def __init__(self):
        self.wrapped_class = BadClass()

    def __getattr__(self, attr):
        orig_attr = self.wrapped_class.__getattribute__(attr)



cam = BadClass()
cam.setAttr('focal', 35)
print(cam.getAttr('focal'))
cam.setAttr('focal', 55)
print(cam.getAttr('focal'))


cam2 = BadClassWrapper()
print(cam2.focal)
cam2.focal = 55
print(cam2.focal)

cam3 = NewWrapper()
