def do_it():
    yield 1
    yield 2

for element in do_it():
    print(element)

# print(dir(do_it()))
# print(help(do_it()))
