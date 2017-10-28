import checks

for name, item in vars(checks).items():
    print name, type(item)
