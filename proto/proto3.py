
class __prot:
    def link(self, other):
        type(self).__bases__ = (type(other),)
        return self

    def __setattr__(self, name, data):
        setattr(type(self), name, data)


def prot(**kwargs):
    prot = type('prot', (__prot,), kwargs.copy())
    return prot()


mikan = prot(name='mikan')
mikan.__str__ = lambda self: self.name
print(mikan)

ajo = prot(name='ajo').link(mikan)
print(ajo)

mikan.put = lambda self: print(self)
ajo.put()
ajo.name

oso = prot(name='oso')
oso.puts = lambda self : print(f"__{self.name}__")

mikan = mikan.link(oso)

ajo.puts()
