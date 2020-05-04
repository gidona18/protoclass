def make(**kwargs):
    "..."
    obj = type('',(object,),{})()
    obj.__dict__ = kwargs
    return obj

print(make(name='self'))
