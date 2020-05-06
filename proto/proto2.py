from types import MethodType

def __soft(self, other):
    pass

def __hard(self, other):
    class prot(other):
        def __getattr__(self, name):
            return "OHNO"
    return prot

def prot(**kwargs):
    class prot:
        def __init__(self, __dict):
            for name in __dict:
                setattr(type(self), name, __dict[name])
        def __setattr__(self, name, data):
            return setattr(type(self), name, data)
        def __getattr__(self, name):
            return getattr(type(self), name)
    return prot(kwargs)





jude = prot(name='jude')
john = prot(name='john')
#jude.age = 21
print(jude.name)

#j = prot().hard(jude)
#print(j.name)
