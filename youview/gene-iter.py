# def do_it():
#     yield 1
#     yield 2

# for element in do_it():
#     print(element)

# print(dir(do_it()))
# print(help(do_it()))

###

import copy

def gen_it(list_):
    for k in list_:
        yield k * 2

a = gen_it([1,2,3])
b = gen_it([1,2,3])

for k in a:
    print(k)

print(b.__next__())
print(b.__next__())
print(b.__next__())
