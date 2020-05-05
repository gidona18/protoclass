# Protobj

```Python
import protobj as pt


# we create a simple object
orange = pt.make(name='orange', color='214')


# later on, we discover its parent, which has functionality
fruit = pt.make()
fruit.str = lambda self: "I AM FRUIT"


# we would like to use that functionality
orange = pt.link(orange, fruit)
orange.str()
# => "I AM FRUIT"


# then, the parent class becomes a little crazy
fruit.str = lambda self: "I AM FRUIT???"


# and the children get confused
orange.str()
# => "I AM FRUIT???"


# and they decide to cut ties with their parents and do their thing
orange = pt.copy(orange, fruit)
orange.str = lambda self: "I AM ORENJI!"

orange.str()
# => "I AM ORENJI!"

fruit.str()
# => "I AM FRUIT???"
# and the porents do their own thing...
```
