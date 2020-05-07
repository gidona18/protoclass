# ---------------------------------------------------------------------


class __proto:
    "Base prototype"

    def link(self, other):
        """Make current object a prototype of another object.
        This is similar to single inheritance. Each object
        can have multiple child links, but only one parent link.
        Parent links can be changed at any time, but objects
        that are children of this one will be affected by this.
        This enables change propagation.
        """
        type(self).__bases__ = (type(other),)  # change parent link
        return self

    def __setattr__(self, name, value):
        return setattr(type(self), name, value)

    def __repr__(self):
        return f"<proto object at {hex(id(self))}>"


def proto(**kwargs):
    """Make a new prototype object with the given attributes.
    If no properties are given, and empty prototype will be created.
    The latter is useful when only a clone of another object is needed.
    """
    return type("proto", (__proto,), kwargs.copy())()


# ---------------------------------------------------------------------
