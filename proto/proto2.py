from inspect import signature
from types import MethodType

#TODO: maybe turn keys into set

class __prot:
    def __init__(self, __dict):
        setattr(type(self), '__prot_keys', list(__dict.keys()))
        for name in __dict:
            setattr(type(self), name, __dict[name])

    def __setattr__(self, name, data):
        getattr(self, '__prot_keys').append(name)
        return setattr(type(self), name, data)
        
    def __getattr__(self, name):
        return getattr(type(self), name)

# ---------------------------------------------------------------------

def link(self, other):
    prot_dict = {}
    for key in getattr(self, '__prot_keys'):
        prot_dict[key] = self.__dict__[key]
    prot = type('prot', (type(other),), {})
    setattr(prot, '__prot_link', other)
    return prot(prot_dict)


def dupe(self, other):
    class prot(__prot):
        pass

    prot_dict = {}
    for key in getattr(self, '__prot_keys'):
        prot_dict[key] = self.__dict__[key]
    prot_link = other
    while prot_link:
        for key in getattr(prot_link, '__prot_keys'):
            if key not in prot_dict:
                val = type(prot_link).__dict__[key]
                print(type(val) == MethodType)
                prot_dict[key] = type(prot_link).__dict__[key]
        prot_link = getattr(prot_link, '__prot_link')

    setattr(prot, '__prot_link', None)
    return prot(prot_dict)


def prot(**kwargs):
    class prot(__prot):
        pass

            
    setattr(prot, 'link', MethodType(link, prot))
    setattr(prot, 'dupe', MethodType(dupe, prot))
    setattr(prot, '__prot_link', None)
    return prot(kwargs)


arm = prot(name='arm')
assert(arm.name == 'arm')
arm.__str__ = MethodType(lambda self: self.name, arm)

cla = prot(age='22').link(arm)
assert(cla.name == 'arm')
assert(cla.age == '22')

ala = prot(color='white').dupe(cla)
assert(ala.color == 'white')
assert(ala.age == '22')
assert(ala.name == 'arm')

arm.name = 'cla'
assert(arm.name == 'cla')
assert(cla.name == 'cla')
assert(cla.age == '22')
cla.age = '23'
assert(cla.age == '23')

assert(ala.color == 'white')
assert(ala.age == '22')
assert(ala.name == 'arm')

#ala.__str__ = MethodType(lambda self: self.color, ala)
ala.name = 'ala'
print(ala)
