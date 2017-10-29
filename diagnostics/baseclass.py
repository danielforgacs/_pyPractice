import abc

class DiagnosticBase(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, reportobj):
        self._report = reportobj

    # @abc.abstractmethod
    def run_test(self):
        return self._report

    @property
    def report(self):
        result = self.run_test()
        if type(result) != type(self._report):
            raise AttributeError('RUN_TEST MUST RETURN REPORT!')
        return result
