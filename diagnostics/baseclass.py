import abc

class DiagnosticBase(object):
    def __init__(self, reportobj):
        self._report = reportobj
    # __metaclass__ = abc.ABCMeta

    def run_test(self):
        pass

    @property
    def report(self):
        return self._report
