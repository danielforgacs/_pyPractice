import baseclass


class CheckFirst(baseclass.DiagnosticBase):
    pass


class EmptyClass(object):
    pass


class SecondExtensionClass(EmptyClass):
    pass
