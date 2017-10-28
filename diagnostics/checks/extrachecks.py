import baseclass


class MiscCheck(baseclass.DiagnosticBase):
    pass


class DetailedClass(object):
    pass


class GuruClass(DetailedClass):
    pass


# print issubclass(CheckSecondExtension, CheckSecond)
# print issubclass(CheckFirst, baseclass.DiagnosticBase)
# print issubclass(CheckSecond, baseclass.DiagnosticBase)
