from inspect import signature
from types import MethodType

class __prot:
    def __setattr__(self, name, data):
        return setattr(type(self), name, data)
        
    def __getattr__(self, name):
        return getattr(type(self), name)

# ---------------------------------------------------------------------

def link(self, other):
    class prot:
        def __init__(self, __dict):
            for name in __dict:
                setattr(type(self), name, __dict[name])
        def __setattr__(self, name, data):
            return setattr(type(self), name, data)
        
        def __getattr__(self, name):
            return getattr(type(self), name)

    prot(type(self).__dict__)
    prot = type('prot', (type(other),), prot.__dict__.copy())
    return prot()


def dupe(self, other):
    class prot(__prot):
        def __init__(self):
            pass

    prot_dict = type(other).__dict__.copy()
    #prot = type('prot', (type(other),), prot.__dict__.copy())
    #prot_link = getattr(type(other), '__prot_link')
    #while prot_link:

    prot_dict.update(type(self))
    setattr(prot, '__prot_link', None)
    return prot()


def prot(**kwargs):
    class prot:
        def __init__(self, __dict):
            for name in __dict:
                setattr(type(self), name, __dict[name])
        def __setattr__(self, name, data):
            return setattr(type(self), name, data)
        
        def __getattr__(self, name):
            return getattr(type(self), name)
            
    setattr(prot, 'link', MethodType(link, prot))
    setattr(prot, 'dupe', MethodType(dupe, prot))
    setattr(prot, '__prot_link', None)
    return prot(kwargs)


arm = prot(name='arm')
print(arm.name)
print()

cla = prot(age='22').link(arm)
print(cla.age)
print()

