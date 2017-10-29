import abc

class DiagnosticBase(object):
    def __init__(self, report):
        self.report = report
    # __metaclass__ = abc.ABCMeta

    def run_test(self):
        pass
