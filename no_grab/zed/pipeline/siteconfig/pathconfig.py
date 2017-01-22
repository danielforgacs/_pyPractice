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

# deployroot needs to be set here hardcoded.
deployroot = 'd:/dev/pyLearn/no_grab/zed/pipeline/library'
# if you want a dev environment,
# set DEVROOT on your machine
devroot = os.environ.get('devroot')
# this probably should go in a config
# file. probably versionconfig.py
# any used module's path needs to be
# listed here. the path is relative
# here from deployed and dev root.
# from devroot and deployroot
# the path hierarchy must be the same.
modules = {'databasetools': 'backend'}
paths = []

if devroot:
    os.sys.path.insert(0, devroot)
    print '--> devroot is set:', devroot

# if there's a dev evn config file
# it will be imported here. devcon.py
# is just a tuple of module names
# to be imported as dev
try:
    import devcon
    print '--> devcon imported.'
except:
    devcon = None
    print '--> no devcon.'

# subversion control is possible
# for frozen static version folders
try:
    import versionconfig
except:
    versionconfig = None

for module in modules:
    # by default all modules are imported
    # as deployed nothing needs to be set up
    # for this to work, except this module.
    root = deployroot
    subversion = ''

    # devcon can be empty
    if hasattr(devcon, 'devimports'):
        # if a module is in dev config
        # root is changed from depolyed
        # to dev root
        if module in devcon.devimports:
            print '--> !!! Module is imported as dev:', module
            root = devroot

    # if the code is deployed it can be
    # subversioned.
    if (root == deployroot) and versionconfig:
        versions = versionconfig.moduleversions

        if module in versions:
            print '--> Old version of this module is in use!'
            print module

            for version in versions[module]:
                print version
                print versions[module][version]
                user = os.environ['username']

                if user in versions[module][version]:
                    subversion = version

    modulepath = os.path.join(root, modules[module], subversion)
    paths.append(modulepath)

print '--> pipeline paths:'
listprint(paths)

os.sys.path.extend(paths)