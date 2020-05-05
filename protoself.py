from copy import deepcopy

"""

class Prototype:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# ---------------------------------------------------------------------

    def __repr__(self):
        try: return self.repr(self)
        except AttributeError: return repr(self.__dict__)

    def __str__(self):
        try: return self.str(self)
        except AttributeError: return str(self.__dict__)

    def __bytes__(self):
        try: return self.bytes(self)
        except AttributeError: return bytes(self.__dict__)

def make(**kwargs):
    return Prototype(**kwargs)

def copy(dst, src):
    # TODO: implement copy on write
    return Prototype(**deepcopy(src.__dict__))

def link(dst, src):
    return Prototype(**src.__dict__)



@attr(mikan, __str__)
def mikan

mikan = make(name='mikan', color='214')
mikan.str = lambda self : \
    f"\u001b[38;5;{self.color}m{self.name}\u001b[0m"

print(repr(mikan))
print(str(mikan))
print()

fruit = make(name='fruit',color='15')
fruit.str = lambda self : \
    f"\u001b[38;5;{self.color}m{self.name}\u001b[0m"

print(repr(fruit))
print(str(fruit))
print()

apple = make()
apple = copy(apple, fruit)
apple.name = 'apple'
apple.color = '9'
print(repr(apple))
print(str(apple))
print()

gapple = link(make(), apple)
gapple.color = '10'
print(gapple)
print(apple)
# not working...

#mikan = make

#mikan = make(name='mikan', color='#ffaf00')
#print(mikan.__dict__)
#print(str(mikan))

"""

class __Prototype:
    "..."
    def __init__(self, __dict, __link=None):
        self.__dict__ = __dict
        self.__link = __link

    def __getattr__(self, name):
        attr = self
        while attr:
            if name in attr.__dict__:
                return attr.__dict__[name]
            attr = attr.__link
        exn = f"object '{hex(id(self))}' has no attribute '{name}'"
        raise AttributeError(exn)



# ---------------------------------------------------------------------

    def __repr__(self):
        try: return self.repr(self)
        except AttributeError: return repr(self.__dict__)

    def __str__(self):
        try: return self.str(self)
        except AttributeError: return str(self.__dict__)

    def __bytes__(self):
        try: return self.bytes(self)
        except AttributeError: return bytes(self.__dict__)


def make(**kwargs):
    return __Prototype(kwargs)

def link(this, that):
    return __Prototype(this.__dict__, that)

#def link(this, that):
#    return Prototype(this.__dict__, that)

#def copy(this, that):
    # TODO: implement COW
#    this_dict = deepcopy(that.__dict__)
#    this_dict.update(this.__dict__)
#    return Prototype(this_dict)

#orenji = make({'name':'orenji'})
orenji = make(name='orenji', color='11')
orenji.str = lambda self:\
    f"\u001b[38;5;{self.color}m{self.name}\u001b[0m"
print(orenji)
print(orenji.name)

aka = link(make(color='9'), orenji)
print(aka)
print(orenji)
print(aka.maru)

#print(orenji.__dict__)

