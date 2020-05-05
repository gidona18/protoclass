from copy import deepcopy

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


"""

@attr(mikan, __str__)
def mikan

"""

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
