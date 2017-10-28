class DiagnosticBase(object):
    pass
    def runner(self, report):
        # return report + '\n' + str(self.__class__)
        return '\n' + str(self.__class__)
