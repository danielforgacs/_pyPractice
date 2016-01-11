a = [1, 2, 3, 4, 5]
a_iter = iter(a)

b = ('a','b','c','d','e')
b_iter = iter(b)

print(type(a), type(a_iter))
print(type(b), type(b_iter))

print(a_iter.__next__())
print(a_iter.__next__())
print(a_iter.__next__())
print(next(a_iter))
print()

next(b_iter)

for k in b_iter:
    print(k)

r = range(5)

# print(type(r))
# print(dir(type(r)))
# print(help(r))

print(r)
print(iter(r))
