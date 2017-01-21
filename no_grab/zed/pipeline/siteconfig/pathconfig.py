"""
siteconfig path must be always visible
from anywhere.

best option: add to PYTHONPATH
"""

import os
# from pprint import pprint

def listprint(list_):
    print '\t'+'\n\t'.join((sorted(list_)))

print '--> default paths:'
listprint(os.sys.path)

deployroot = 'd:/dev/pyLearn/no_grab/zed/pipeline/library'
# databasetools = 'd:/dev/pyLearn/no_grab/zed/pipeline/library/backend'
# os.sys.path.append(databasetools)
modules = {'databasetools': 'backend'}
paths = []

for module in modules:
    root = deployroot
    modulepath = os.path.join(root, modules[module])
    paths.append(modulepath)

print '--> pipeline paths:'
listprint(paths)

os.sys.path.extend(paths)
