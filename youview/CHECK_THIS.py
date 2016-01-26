class MyInt(object):

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def __lt__(self, rhs):
        return self.val1 < rhs.val1

max([MyInt(10, 1),  MyInt(5, 1), MyInt(50, 1), MyInt(-5, 1)])
>> MyInt(50, 1)
