def g():
    a = 10

    while a > 0:
        yield a
        a -= 1



for j in g():
    print(j)
