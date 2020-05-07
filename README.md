protoclass
=========
![PyPi](https://badge.fury.io/py/protoclass.svg)
![PyVersions](https://img.shields.io/pypi/pyversions/protoclass.svg)

Prototype-Oriented Programming in Python.

Installation
------------
`pip install protoclass`

Usage
-----
```Python
from protoclass import proto

# We create a basic object and add some functionality
jane = proto(first="Jane", last="Doe")
jane.greet = lambda self: print(self)
jane.greet()
# >>> <proto object at ...>

# Oh no, we want something prettier...
# We could modify the `greet` function...
# Or we could create a `person` object an inherit from it
person = proto(first="", last="")
person.__str__ = lambda self: f"{self.first} {self.last}"
jane.link(person)

# Now we get a nicer greeting
jane.greet()
# >>> Jane Doe
```

API Reference
-------------
**`proto(**kwargs)`**
Make a new prototype object with the given attributes. If no properties are given, and empty prototype will be created. The latter is useful when only a clone of another object is needed.

**`proto.link(self, other)`** Make current object a prototype of another object. This is similar to single inheritance. Each object can have multiple child links, but only one parent link. Parent links can be changed at any time, but objects that are children of this one will be affected by this. This enables change propagation.

License
-------
[Apache-2.0](./LICENSE)
