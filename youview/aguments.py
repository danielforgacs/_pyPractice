def simplest(*args):
    return args


def exxxxtra(**kwargs):
    return kwargs


a = simplest()
print(a, type(a))

a = simplest('a', 1, float)
print(a, type(a))

b = exxxxtra()
print(b, type(b))

b = exxxxtra(a=1, b=float, h='##a')
print(b, type(b))
