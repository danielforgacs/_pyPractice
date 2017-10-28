import db

class Pros(object):
    def __get__(self, obj, objtype):
        sgpros = obj.sg.query(
            dbtype='PROS',
            filter=[])
        pros = []
        for prodict in sgpros:
            prodict['sg'] = obj.sg
            newpro = Pro(**prodict)
            pros.append(newpro)
        return pros


class Varis(object):
    def __get__(self, obj, objtype):
        sgvaris = obj.sg.query(
            dbtype='VARIS',
            filter=[])
        varis = []
        for varidict in sgvaris:
            varidict['sg'] = obj.sg
            newvari = Vari(**varidict)
            varis.append(newvari)
        return varis


class Asses(object):
    def __get__(self, obj, objtype):
        sgasses = obj.sg.query(
            dbtype='ASSES',
            filter=[])
        asses = []
        for assdict in sgasses:
            assdict['sg'] = obj.sg
            newass = Ass(**assdict)
            asses.append(newass)
        return asses


class Pubs(object):
    def __get__(self, obj, objtype):
        sgpubs = obj.sg.query(
            dbtype='PUBS',
            filter=[])
        pubs = []
        for pubdict in sgpubs:
            pubdict['sg'] = obj.sg
            newpub = pubdict
            # newpub = Ass(**pubdict)
            pubs.append(newpub)
        return pubs


class Pro(object):
    varis = Varis()

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
    def __repr__(self):
        return '{} {}'.format(
            self.name, self.id)
    def __iter__(self):
        return iter(self.varis)
    def __getitem__(self, index):
        return self.varis[index]


class Vari(object):
    asses = Asses()

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
    def __str__(self):
        return '{} {} {}'.format(
            self.name,
            self.id,
            self.area)
    def __getitem__(self, index):
        return self.asses[index]


class Ass(object):
    pubs = Pubs()

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
    def __str__(self):
        return '{} {} {}'.format(
            self.name,
            self.id,
            self.colour)
    def __iter__(self):
        return iter(self.pubs)


class SG(object):
    pros = Pros()
    def __init__(self, name, pid, key):
        pass
    def __iter__(self):
        return iter(self.pros)
    def query(self, dbtype, filter, fileds=None):
        return getattr(db, dbtype)
    def __getitem__(self, index):
        return self.pros[index]
    @property
    def sg(self):
        return self


if __name__ == '__main__':
    sg = SG(name='name', pid=555, key='4f*7')

    for pro in sg:
        print '--> Pro:', pro

        print '\t--> Varis:'
        for vari in pro:
            print '\t\t', vari

            print '\t\t--> asses:'
            for ass in vari:
                print '\t\t\t', ass

                print '\t\t\t--> pubs:'
                for pub in ass:
                    print '\t\t\t\t', pub

            print
