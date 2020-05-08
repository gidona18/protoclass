"""

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

"""
