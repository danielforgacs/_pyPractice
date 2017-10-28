import abc

class DiagnosticBase(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def runner(self, report):
        return str(self.__class__)
