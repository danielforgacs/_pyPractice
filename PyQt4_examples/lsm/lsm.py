test_data = zip(list('abcdefgh'), list('qwertypo'))


def get_data():
    for element in test_data:
        yield element


data = get_data()

print next(data)
print next(data)
print next(data)
