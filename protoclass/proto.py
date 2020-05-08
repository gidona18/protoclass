# ---------------------------------------------------------------------


def chain(self, other):
    """Makes self inherit from a single prototype.

    Any relationship with previous parent prototypes will be removed.

    Parameters
    ----------
    other : proto
        Prototype to inherit attributes from.

    Returns
    -------
    self : proto
        A proto object that inherits from `other`.

    Raises
    ------
    TypeError
        When trying to chain self to self because it generates a cycle.

    Examples
    --------
    >>> tangerine = proto(color="orange")
    >>> orange = proto().chain(tangerine)
    >>> orange.color
    'orange'

    """

    type(self).__bases__ = (type(other),)
    return self


def multichain(self, *others):
    """Makes self inherit from multiple prototypes.

    Any relationship with previous parent prototypes will be removed.
    When the parent prototypes share attributes with the same name, the
    parent prototype that is first in the list of prototypes will
    provide it.

    Parameters
    ----------
    *others : iterable
        Prototypes to inherit attributes from.

    Returns
    -------
    self : proto
        A proto object that inherits from `others`.

    Raises
    ------
    TypeError
        When trying to chain self to self because it generates a cycle.

    Examples
    --------
    >>> cat = proto(name="cat", meow="meow")
    >>> dog = proto(name="dog", bark="woof")
    >>> catdog = proto(color="orange").multichain(cat, dog)
    >>> catdog.color
    'orange'
    >>> catdog.meow
    'meow'
    >>> catdog.bark
    'woof'
    >>> catdog.name  # first attribute found will be used upon conflict
    'cat'

    """

    bases = ()
    for other in others:
        bases = bases + (type(other),)
    type(self).__bases__ = type(self).__bases__ + bases
    return self


def proto(**attrs):
    """Makes a new proto object with given attributes.

    When no attributes are given, an empty object will be made.

    Parameters
    ----------
    **attrs : dict
        Attributes to add to `proto`.

    Returns
    -------
    proto : proto
        A new proto object with given attributes.

    Examples
    --------
    >>> jane = proto(first='Jane', last='Doe')
    >>> f"{jane.first} {jane.last}"
    'Jane Doe'
    >>> null = proto()
    >>> null  #doctest: +ELLIPSIS
    <proto object at ...>

    """

    class __proto:
        def __setattr__(self, name, value):
            return setattr(type(self), name, value)

        def __repr__(self):
            return f"<proto object at {hex(id(self))}>"

    ty = type("proto", (__proto,), attrs.copy())
    setattr(ty, "chain", chain)
    setattr(ty, "multichain", multichain)
    return ty()


def clone(proto_object):
    """Makes a new proto object that inherits from a single prototype.

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
    """Makes a new proto object that inherits from multiple prototypes.

    Equivalent to proto().multichain(`proto_objects`).
    When the parent prototypes share attributes with the same name, the
    parent prototype that is first in the list of prototypes will
    provide it.

    Parameters
    ----------
    proto_objects : iterable
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


# ---------------------------------------------------------------------
