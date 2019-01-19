import baseclass


class CheckFirst(baseclass.DiagnosticBase):
    pass
    def run_test(self, report):
        report.text += '\nfdsaggka'
        return report

# # class EmptyClass(object):
# #     pass

# # class SecondExtensionClass(EmptyClass):
# #     pass
