"""
siteconfig path must be always visible
from anywhere. best option: add to PYTHONPATH

to set up a machine as dev, create
an env var called DEVROOT with the
path you want to work in.
"""

import os

def listprint(list_):
    print '\t'+'\n\t'.join((sorted(list_)))

print '--> default paths:'
listprint(os.sys.path)

deployroot = 'd:/dev/pyLearn/no_grab/zed/pipeline/library'
devroot = os.environ.get('devroot')
modules = {'databasetools': 'backend'}
paths = []

if devroot:
    os.sys.path.insert(0, devroot)
    print '--> devroot is set:', devroot

try:
    import devcon
except:
    devcon = None

for module in modules:
    root = deployroot

    if hasattr(devcon, 'devimports'):
        if module in devcon.devimports:
            print '--> !!! Module is imported as dev:', module
            root = devroot

    modulepath = os.path.join(root, modules[module])
    paths.append(modulepath)

print '--> pipeline paths:'
listprint(paths)

os.sys.path.extend(paths)