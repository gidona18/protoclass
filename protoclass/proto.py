# ---------------------------------------------------------------------

def __chain(self, other):
    """..."""
    # will raise TypeError if linking self
    type(self).__bases__ = (type(other),)
    return self

def __multichain(self, *others):
    """..."""
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
    #return type("proto", (__Proto,), kwargs.copy())()


def clone(proto_object):
    """..."""
    return proto().chain(proto_object)


# what if some objects should not be cloned?


# ---------------------------------------------------------------------
