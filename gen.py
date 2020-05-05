lst = r"""
repr
str
bytes
format
lt
le
eq
ne
gt
ge
hash
bool
"""

const = """
new
init
del
getattr
getattribute
setattr
delattr
dir
get
set
delete
set_name
slots
init_subclass
mro_entries
class
instancecheck
subclasscheck
class_getitem
call
len
length_hint
getiten
setitem
delitem
missing
iter
reversed
contains
add
sub
mul
matmul
truediv
floordiv
mod
divmod
pow
lshift
rshift
and
xor
or
radd
rsub
rmul
rmatmul
rtruediv
rfloordiv
rmod
rdivmod
rpow
rlshift
rrshift
rand
rxor
ror
iadd
isub
imul
imatmul
itruediv
ifloordiv
imod
ipow
ilshift
irshift
iand
ixor
ior
neg
pos
abs
invert
complex
int
float
index
round
trunc
floor
ceil
enter
exit
await
send
throw
close
aiter
anext
aenter
aexit
"""

now = """
repr
str
bytes
"""


def make_code(source):
    funs = source.split()
    for f in funs:
        print(
            f"""\
def __{f}__(self):
    try: return self.{f}(self)
    except AttributeError: return {f}(self.__dict__)
"""
        )


make_code(now)
