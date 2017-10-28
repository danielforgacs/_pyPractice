import abc

class DiagnosticBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def runner(self, report):
        pass
