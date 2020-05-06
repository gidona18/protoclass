class Prot:
    def __init__(self):
        pass
    def __call__(self, **kwargs):
        class prot(Prot):
            def __init__(self, __dict):
                self.__dict__.update(__dict)
        return prot(kwargs)

prot = Prot()

jude = prot(name='jude')
john = prot(name='john')
print(type(jude) == type(john))
