# ---------------------------------------------------------------------


import warnings


# ---------------------------------------------------------------------


def chain(self, other, *others):
    """Makes self copy attributes from another prototype or multiple other prototypes.

    Any previous relationship with other parent prototypes will be
    automatically severed.

    When parent prototypes share attributes with the same name, the
    first parent prototype that has that attribute will be provide it,
    so the order in which they are given matters.

    Any change made to parent prototypes will be automatically
    propagated to this prototype.

    Parameters
    ----------
    other: proto
        Prototype to copy attributes from.

    *others : list(proto)
        Prototypes to copy attributes from.

    Returns
    -------
    self : proto
        A prototype with attributes from `other` and `others`.

    Raises
    ------
    TypeError
        When trying to chain `self` to `self` as it causes a cycle.

    Examples
    --------
    >>> tangerine = proto(color="orange")
    >>> orange = proto().chain(tangerine)
    >>> orange.color
    'orange'
    >>> cat = proto(name="cat", meow="meow")
    >>> dog = proto(name="dog", bark="woof")
    >>> catdog = proto(color="orange").multichain(cat, dog)
    >>> catdog.color
    'orange'
    >>> catdog.meow
    'meow'
    >>> catdog.bark
    'woof'
    >>> catdog.name
    'cat'

    """

    bases = (type(other),)
    for other in others:
        bases = bases + (type(other),)
    type(self).__bases__ = bases
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

    .. deprecated:: 0.5.3
       `multichain` will be removed in protoclass 1.0.0, and it will
       be replaced by `chain` because the latter now works with
       multiple prototypes as well.

    """

    warnings.warn(
        "Deprecated since version 0.5.3: `multichain` will be removed in protoclass 1.0.0, and it will be replaced by `chain` because the latter now works with multiple prototypes as well.",
        DeprecationWarning,
    )

    bases = ()
    for other in others:
        bases = bases + (type(other),)
    type(self).__bases__ = type(self).__bases__ + bases
    return self


def proto(**attrs):
    """Makes a new prototype with given attributes.

    An empty prototype will be made when no attributes are given.

    Parameters
    ----------
    **attrs : dict
        Attributes to add to `proto`.

    Returns
    -------
    proto : proto
        A new prototype with given attributes.

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


def clone(other, *others):
    """Makes a new prototype by copying attributes from another prototype or multiple other prototypes.

    When parent prototypes share attributes with the same name, the
    first parent prototype that has that attribute will be provide it,
    so the order in which they are given matters.

    Any change made to parent prototypes will be automatically
    propagated to this clone.

    Equivalent to ``proto().chain(other, *others)``

    Parameters
    ----------
    other: proto
        Prototype to copy attributes from.

    *others : list(proto)
        Prototypes to copy attributes from.

    Returns
    -------
    proto : proto
        A new prototype with attributes from `other` and `others`.

    Examples
    --------
    >>> apple = proto(kind="fruit", color="green")
    >>> mango = clone(apple)
    >>> mango.kind
    'fruit'
    >>> mango.color
    'green'
    >>> cat = proto(name="cat", meow="meow")
    >>> dog = proto(name="dog", bark="woof")
    >>> catdog = multiclone(cat, dog)
    >>> catdog.meow
    'meow'
    >>> catdog.bark
    'woof'
    >>> catdog.name
    'cat'

    """

    return proto().chain(other, *others)


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

    .. deprecated:: 0.5.3
       `multiclone` will be removed in protoclass 1.0.0, and it will
       be replaced by `clone` because the latter now works with
       multiple prototypes as well.

    """

    warnings.warn(
        "Deprecated since version 0.5.3: `multiclone` will be removed in protoclass 1.0.0, and it will be replaced by `clone` because the latter now works with multiple prototypes as well.",
        DeprecationWarning,
    )

    return proto().multichain(*proto_objects)


# ---------------------------------------------------------------------
