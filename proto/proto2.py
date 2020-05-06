from inspect import signature
from types import MethodType

class __prot:
    def __setattr__(self, name, data):
        return setattr(type(self), name, data)
        
    def __getattr__(self, name):
        return getattr(type(self), name)


def __link(self, other):
    class prot(__prot):
        def __init__(self):
            pass

    prot = type('prot', (type(other),), prot.__dict__.copy())
    return prot()


def __copy(self, other):
    class prot:
        def __init__(self):
            pass
        
        def __setattr__(self, name, data):
            return setattr(type(self), name, data)
        
        def __getattr__(self, name):
            return getattr(type(self), name)

    prot = type('prot', (type(other),), prot.__dict__.copy())
    return prot()


def prot(**kwargs):
    class prot(__prot):
        def __init__(self, __dict):
            for name in __dict:
                setattr(type(self), name, __dict[name])
            
    setattr(prot, 'link', MethodType(__link, prot))
    setattr(prot, 'copy', MethodType(__copy, prot))
    return prot(kwargs)




jude = prot(name='jude')
jay = prot().link(jude)
print(jay.name)

jude.name = 'jude2'
print(jay.name)

jay.name = 'jay'
jude.name = 'jude'
print(jude.name)
print(jay.name)
