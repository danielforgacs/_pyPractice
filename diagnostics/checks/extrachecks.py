import baseclass


class MiscCheck(baseclass.DiagnosticBase):
    def runner(self, report):
        return str(self)

class DetailedClass(object):
    pass


class GuruClass(DetailedClass):
    pass
