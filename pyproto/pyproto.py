class __proto:
    def link(self, other):
        type(self).__bases__ = (type(other),)
        return self
    
    def __setattr__(self, name, value):
        return setattr(type(self), name, value)

def proto(**kwargs):
    return type('proto', (__proto), kwargs.copy())

# ---------------------------------------------------------------------
#
# ---------------------------------------------------------------------

import unittest

class TestCase(unittest.TestCase):
    def single_proto(self):
        # members
        mikan = proto(name='mikan')
        self.assertEqual(mikan.name, 'mikan')
        mikan.color = 'orange'
        self.assertEqual(mikan.color, 'color')
        mikan.type = 'fruit'
        self.assertEqual(mikan.type, 'fruit')
        # methods
        mikan.__str__ = lambda self: self.name
        self.assertEqual(str(mikan), mikan.name)
        self.assertEqual(mikan.__str__(), mikan.name)
        mikan.introduce = lambda self: f"watashi wa {self.name} desu!"
        self.assertEqual(mikan.introduce(), "watashi wa mikan desu!")



if __name__ == '__main__':
    unittest.main()
