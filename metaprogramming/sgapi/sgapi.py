PROS = (
    {'name': 'pro0', 'id': 0},
    {'name': 'pro1', 'id': 1},
    {'name': 'pro2', 'id': 2},
)
VARS = [
]


class Pros(object):
    def __get__(self, obj, objtype):
        sgpros = obj.query(dbtype='PROS', filter=[])
        pros = []
        for prodict in sgpros:
            newpro = Pro(**prodict)
            pros.append(newpro)
        return pros


class Varis(object):
    def __get__(self, obj, objtype):
        return [1, 2, 3]


class Pro(object):
    varis = Varis()

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
    def __repr__(self):
        return '{} {}'.format(self.name, self.id)
    def __iter__(self):
        return iter(self.varis)


class SG(object):
    pros = Pros()
    def __init__(self, name, pid, key):
        pass
    def __iter__(self):
        return iter(self.pros)
    def query(self, dbtype, filter, fileds=None):
        return globals().get(dbtype)
    def __getitem__(self, index):
        return self.pros[index]


if __name__ == '__main__':
    sg = SG(name='name', pid=555, key='4f*7')

    print sg[1:3]
    print sg[0]

    for pro in sg:
        print '--> Pro:\n\t', pro

        print '\t--> Varis:'
        for vari in pro:
            print '\t\t\t', vari
