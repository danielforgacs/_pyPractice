import checks
import types
import baseclass

for name, item in vars(checks).items():
    if isinstance(item, types.ModuleType):
        for key, value in vars(item).items():
            if not key.startswith('_'):
                pass


modules = [module for module in vars(checks).values()
            if isinstance(module, types.ModuleType)]
print modules

