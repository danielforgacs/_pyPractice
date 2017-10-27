PROS = [
    {'name': 'pro0', 'id': 0},
    {'name': 'pro1', 'id': 1},
    {'name': 'pro2', 'id': 2},
]

class Pros(object):
    def __get__(self, obj, objtype):
        pros = obj.query(dbtype='PROS', filter=[])
        return pros

class SG(object):
    pros = Pros()
    def __init__(self, name, pid, key):
        pass
    def __iter__(self):
        return iter(self.pros)
    def query(self, dbtype, filter, fileds=None):
        return globals().get(dbtype)





if __name__ == '__main__':
    sg = SG(name='name', pid=555, key='4f*7')

    for pro in sg:
        print pro
