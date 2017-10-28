import baseclass


class MiscCheck(baseclass.DiagnosticBase):
    pass


class DetailedCheck(object):
    pass


class GuruCheck(DetailedCheck):
    pass


# print issubclass(CheckSecondExtension, CheckSecond)
# print issubclass(CheckFirst, baseclass.DiagnosticBase)
# print issubclass(CheckSecond, baseclass.DiagnosticBase)
