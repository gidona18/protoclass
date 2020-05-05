from copy import deepcopy

class Proto:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.__link = None

    def link(self, other):
        self.__link = other
        return self

    def copy(self, other):
        #self_dict = deepcopy(other.__dict__)
        #self_dict.update(sefl.__dict__)
        #sefl.__dict__ = self_dict
        return self

# ---------------------------------------------------------------------

    def __getattr__(self, name):
        attr = self
        while attr:
            if name in attr.__dict__:
                return attr.__dict__[name]
            attr = attr.__link
        exn = "<proto object at {}> has no attribute '{}'>"
        raise AttributeError(exn.format(hex(id(self)), name))

# ---------------------------------------------------------------------



mikan = Proto(name='mikan', color='11')
print(mikan.name, mikan.color)
print()

orenji = Proto(name='orenji').link(mikan)
print(orenji.name, orenji.color)
print(mikan.name, mikan.color)
print()

#tomato = Proto(name='tomato').copy(orenji)
mikan.color = '9'
print(mikan.name, mikan.color)
print(orenji.name, orenji.color)
#print(tomato.name, tomato.color)
print()
