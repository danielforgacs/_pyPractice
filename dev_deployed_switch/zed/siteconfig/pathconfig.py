"""
this module needs to be always accesible
and imported first.

if you want to switch from deployed
to dev put a tuple with module
names in it called devimports
in a python module called devcon.py

save it in the dev folder root

dev root comes from the env var
"devroot"
"""


import sys
from os.path import join as joinpath
from os import environ as envvar

# set deployed and dev paths
# set up user dev roots with an env var
deployedroot = 'd:/dev/pyLearn/dev_deployed_switch/zed'
devroot = envvar.get('devroot')

sys.path.insert(0, devroot)

# import user module containing
# modules to be used as dev
try:
    from devcon import devimports
    sys.path.pop(0)
except:
    devimports = ()


# module relative paths
# for packages use containing path
modules = {'backend': 'lib/backend'}

# add module paths to sys.path
for module in modules:
    root = deployedroot

    if module in devimports:
        root = devroot
        print '..> dev mode import:', module

    sys.path.append(joinpath(root, modules[module]))
