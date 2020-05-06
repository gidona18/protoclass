class X:
    def __init__(self, x):
        self.x = x

x = X(10)
x.put = (lambda self: print(self.x)).__get__(x)

#x.put()


class __prot:
    def link(self, other):
        prot = type('prot', (type(other),), type(self).__dict__.copy())
        return prot()

    def __setattr__(self, name, data):
        if type(data) == type(lambda:None):
            data = data.__get__(self)#XXX:DOES NOT WORK
        setattr(type(self), name, data)

    def __getattr__(self, name):
        return getattr(type(self), name)


def prot(**kwargs):
    return type('prot', (__prot,), kwargs.copy())()

mikan = prot(name='mikan')
#print(mikan.name)
mikan.__str__ = lambda self: mikan.name
print(mikan)

ajo = prot(name='ajo').link(mikan)
print(ajo)
#mikan.__str__.__set__(None)
#ajo.__str__ = mikan.__str__.unbind()
#print(ajo)
#print(dir(ajo.__str__))
