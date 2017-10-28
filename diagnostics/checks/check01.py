import baseclass


class CheckFirst(baseclass.DiagnosticBase):
    def runner(self, report):
        return str(self)

class EmptyClass(object):
    pass


class SecondExtensionClass(EmptyClass):
    pass
