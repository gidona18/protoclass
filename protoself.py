def make(**kwargs):
    "..."
    obj = type('',(object,),{})()
    obj.__dict__ = kwargs
    return obj

orenji = make(name='orenji', color='#FFA500')
print(orenji.__dict__)
