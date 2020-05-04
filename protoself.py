def make(**kwargs):
    "..."
    obj = type('',(object,),{})()
    obj.__dict__.update(kwargs)
    return obj

print(make(name='self'))
