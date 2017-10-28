import baseclass


class CheckFirst(baseclass.DiagnosticBase):
    pass


class CheckSecond(object):
    pass


class CheckSecondExtension(CheckSecond):
    pass


# print issubclass(CheckSecondExtension, CheckSecond)
# print issubclass(CheckFirst, baseclass.DiagnosticBase)
# print issubclass(CheckSecond, baseclass.DiagnosticBase)
