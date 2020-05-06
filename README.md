classless
=========
Prototype-Oriented Programming in Python
----------------------------------------

```Python
from classless import proto

# We create a basic object and add some functionality
jane = proto(first='Jane', last='Doe')
jane.greet = lambda self: print(self)
jane.greet()
# >>> <proto object at 0x7fe062ebdf10>

# Oh no, we want something prettier...
# We could modify the `greet` function...
# Or we could create a `person` object an inherit from it
person = proto(first='', last='')
person.__str__ = lambda self: f'{self.first} {self.last}'
jane.link(person)

# Now we get a nicer greeting
jane.greet()
# >>> Jane Doe

```
