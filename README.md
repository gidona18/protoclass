protoclass
==========
![PyPi](https://badge.fury.io/py/protoclass.svg)
![PyVersions](https://img.shields.io/pypi/pyversions/protoclass.svg)

Prototype-Oriented Programming in Python.

Installation
------------
`pip install protoclass`

Usage
-----
```Python

>>> from protoclass import proto

# We create a basic object and add some functionality
>>> jane = proto(first="Jane", last="Doe")
>>> jane.greet = lambda self: print(self)
>>> jane.greet()  #doctest: +ELLIPSIS
<proto object at ...>


# A more user-friendly would be better.
# We could modify the `greet` function
# or we could create another object and inherit from it
>>> person = proto(first="", last="")
>>> person.__str__ = lambda self: f"{self.first} {self.last}"
>>> jane = jane.chain(person)


# and we should get a better message.
>>> jane.greet()
Jane Doe

```

API Reference
-------------
| |
| --- |
| **`proto(**attrs)`** |
| Makes a new proto object with given attributes. When no attributes are given, an empty object will be made. |
| **`proto.chain(self, other)`** |
| Makes self inherit from a single prototype. Any relationship with previous parent prototypes will be removed. |
| **`proto.multichain(self, *others)`** |
| Makes self inherit from multiple prototypes. Any relationship with previous parent prototypes will be removed. When the parent prototypes share attributes with the same name, the parent prototype that is first in the list of prototypes will provide it. |
| |


License
-------
[Apache-2.0](./LICENSE)
