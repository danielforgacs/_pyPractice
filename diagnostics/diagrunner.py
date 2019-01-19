import checks
import types
import baseclass


class Report(object):
    def __init__(self):
        self.text = '.start.'

report = Report()

for check in baseclass.DiagnosticBase.__subclasses__():
    c = check(report=report)
    report = c.report

print(report.text)
