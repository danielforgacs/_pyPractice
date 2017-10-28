import checks
import types
import baseclass


checklist = []

for name, item in vars(checks).items():
    if isinstance(item, types.ModuleType):
        for key, value in vars(item).items():
            if key.startswith('_'):
                continue
            if isinstance(value, types.ModuleType):
                continue
            if issubclass(value, baseclass.DiagnosticBase):
                checklist.append(value)


print checklist
