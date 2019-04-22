def g():
    a = 10

    while a > 0:
        yield a
        a -= 1


class G(object):
    def __iter__(self):
        return iter(list('abcds'))


class F(object):
    def __next__(self):
        yield 1
    # def __iter__(self):
    #     return iter(list('abcds'))



for k in G():
    print(k)


# for k in F():
#     print(k)

qw = F()
print(next(qw))