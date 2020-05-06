
class __prot:
    def link(self, other):
        prot = type('prot', (type(other),), type(self).__dict__.copy())
        type(self) = prot
        return prot()

    def __setattr__(self, name, data):
        setattr(type(self), name, data)

    def __getattr__(self, name):
        return getattr(type(self), name)


def prot(**kwargs):
    return type('prot', (__prot,), kwargs.copy())()


mikan = prot(name='mikan')
mikan.__str__ = lambda self: self.name
print(mikan)

ajo = prot(name='ajo').link(mikan)
print(ajo)

mikan.put = lambda self: print(self)
ajo.put()

oso = prot(name='oso')
oso.puts = lambda self : print("___")

mikan = mikan.link(oso)

# how to make this work?
#ajo.puts()
