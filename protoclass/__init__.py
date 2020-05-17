# ---------------------------------------------------------------------
# protoclass
# ---------------------------------------------------------------------


__version__ = "0.5.4"


from .proto import proto, clone, chain

proto = proto
clone = clone
chain = chain


# XXX: deprecated in 0.5.3, removed in 1.0.0

from .proto import multiclone, multichain

multiclone = multiclone
multichain = multichain
