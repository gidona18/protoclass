# ---------------------------------------------------------------------

def __chain(self, other):
        """...""" # wil raise TypeError if linking self
        type(self).__bases__ = (type(other),)
        return self



def __multichain(self, *others):
    """...""" # wil raise TypeError if linking self
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
    setattr(ty, 'chain', __chain)
    setattr(ty, 'multichain', __multichain)
    return ty()


def clone(other):
    """..."""
    return proto().chain(other)


def multiclone(*others):
    return proto().multichain(*others)


# what if some objects should not be cloned?


# ---------------------------------------------------------------------
