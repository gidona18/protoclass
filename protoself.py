def make(**kwargs):
    "..."
    obj = type('',(object,),{})()
    obj.__dict__.update(kwargs)
    return obj

class Pt:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        try:
            return str(self)
        except:
            print("OHNO")
        return str(self.__dict__)

    def __setattr__(self, name, data):
        self.__dict__[name] = data

mikan = Pt(name='mikan', color='214')
mikan.str = lambda : f"\u001b[38;5;214m{self.name}\u001b[0m"

print(mikan.str())

#mikan = make(name='mikan', color='#ffaf00')
#print(mikan.__dict__)
#print(str(mikan))
