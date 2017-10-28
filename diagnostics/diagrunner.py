import checks
import types

for name, item in vars(checks).items():
    if isinstance(item, types.ModuleType):
        for key, value in vars(item).items():
            print key, isinstance(key, object)
