import abc

class ReportDescriptor(object):
    def __set__(self, obj, value):
        print '--setting report', obj
        result = obj.run_test(report=value)
        obj.__dict__['report'] = result

    def __get__(self, obj, objtype):
        print '--getting report', obj
        return obj.__dict__['report']


class DiagnosticBase(object):
    # __metaclass__ = abc.ABCMeta
    report = ReportDescriptor()

    def __init__(self, report):
        self.report = report

    # @abc.abstractmethod
    # def run_test(self):
    #     pass
