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
            return self.str(self)
        except AttributeError:
            return str(self.__dict__)

"""

@attr(mikan, __str__)
def mikan

"""

mikan = Pt(name='mikan', color='214')
mikan.str = lambda self : f"\u001b[38;5;214m{self.name}\u001b[0m"

print(mikan)

#mikan = make(name='mikan', color='#ffaf00')
#print(mikan.__dict__)
#print(str(mikan))
