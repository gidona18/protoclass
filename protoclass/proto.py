# ---------------------------------------------------------------------


def __chain(self, other):
    """..."""  # wil raise TypeError if linking self
    type(self).__bases__ = (type(other),)
    return self


def __multichain(self, *others):
    """..."""  # wil raise TypeError if linking self
    bases = ()
    for other in others:
        bases = bases + (type(other),)
    type(self).__bases__ = type(self).__bases__ + bases
    return self


def proto(**attrs):
    """..."""

    class __proto:
        def __setattr__(self, name, value):
            return setattr(type(self), name, value)

        def __repr__(self):
            return f"<proto object at {hex(id(self))}>"

    ty = type("proto", (__proto,), attrs.copy())
    setattr(ty, "chain", __chain)
    setattr(ty, "multichain", __multichain)
    return ty()


def clone(proto_object):
    """Make a new object that inherits from a single prototype.

    Equivalent to proto().chain(`proto_object`).

    Parameters
    ----------
    *proto_object : proto
        Prototype to inherit attributes from.

    Returns
    -------
    proto : proto
        A new object that inherits from `proto_object`.

    Examples
    --------
    >>> apple = proto(kind="fruit", color="green")
    >>> mango = clone(apple)
    >>> mango.kind
    'fruit'
    >>> mango.color
    'green'

    """

    return proto().chain(proto_object)


def multiclone(*proto_objects):
    """Make a new object that inherits from multiple prototypes.

    Equivalent to proto().multichain(*`proto_objects`).
    When the parent prototypes share attributes with the same name, the
    parent prototype that is first in the list of prototypes will
    provide it.

    Parameters
    ----------
    *proto_objects : iterable
        Prototypes to inherit attributes from.

    Returns
    -------
    proto : proto
        A new object that inherits from `proto_objects`.

    Examples
    --------
    >>> cat = proto(name="cat", meow="meow")
    >>> dog = proto(name="dog", bark="woof")
    >>> catdog = multiclone(cat, dog)
    >>> catdog.meow
    'meow'
    >>> catdog.bark
    'woof'
    >>> catdog.name  # first attribute found will be used upon conflict
    'cat'

    """

    return proto().multichain(*proto_objects)


# what if some objects should not be cloned?


# ---------------------------------------------------------------------
