protoclass
==========
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI-downloads-month](https://img.shields.io/pypi/dm/protoclass.svg)](https://pypi.python.org/pypi/protoclass/)
[![PyPI-package-version](https://img.shields.io/pypi/v/protoclass.svg)](https://pypi.python.org/pypi/protoclass/)
[![PyPI-license](https://img.shields.io/pypi/l/protoclass.svg)](https://pypi.python.org/pypi/protoclass/)
[![PyPI-python-versions](https://img.shields.io/pypi/pyversions/protoclass.svg)](https://pypi.python.org/pypi/protoclass/)

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
| **`clone(proto_object)`** |
| Makes a new proto object that inherits from a single prototype. Equivalent to `proto().chain(proto_object)`. |
| **`multiclone(*proto_objects)`** |
| Makes a new proto object that inherits from multiple prototypes. Equivalent to `proto().multichain(proto_objects)`. When the parent prototypes share attributes with the same name, the parent prototype that is first in the list of prototypes will provide it. |
| |

For more information on these functions, call `help` on the function you would like to know more of, like this: `help(proto)`.

License
-------
[Apache-2.0](./LICENSE)
