# ---------------------------------------------------------------------


class __proto:
    def link(self, other):
        type(self).__bases__ = (type(other),)
        return self

    def __setattr__(self, name, value):
        return setattr(type(self), name, value)


def proto(**kwargs):
    return type("proto", (__proto,), kwargs.copy())()


# ---------------------------------------------------------------------
