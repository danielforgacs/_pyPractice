import random

list_ = [random.choice(range(100)) for k in range(10)]

min_ = lambda x: sorted(x)[0]
max_ = lambda x: sorted(x)[len(x)-1]

print(min(list_), min_(list_))
print(max(list_), max_(list_))
