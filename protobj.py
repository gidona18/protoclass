# =====================================================================
# Import
# =====================================================================


from copy import deepcopy


# =====================================================================
# Class
# =====================================================================


class __Proto:
    "..."

    def __init__(self, keys, __link=None):
        self.__dict__ = keys
        self.__link = __link

    def __getattr__(self, name):
        attr = self
        while attr:
            if name in attr.__dict__:
                return attr.__dict__[name]
            attr = attr.__link
        raise AttributeError(
            "<Proto object at {}> has no attribute '{}'".format(hex(id(self)), name)
        )

    def __repr__(self):
        try:
            return self.repr(self)
        except AttributeError:
            return repr(self.__dict__)

    def __str__(self):
        try:
            return self.str(self)
        except AttributeError:
            return str(self.__dict__)

    def __bytes__(self):
        try:
            return self.bytes(self)
        except AttributeError:
            return bytes(self.__dict__)


# =====================================================================
# API
# =====================================================================


def make(**kwargs):
    return __Proto(kwargs)


def link(this, that):
    return __Proto(this.__dict__, that)


def copy(this, that):
    this_dict = deepcopy(that.__dict__)
    this_dict.update(this.__dict__)
    return __Proto(this_dict)
