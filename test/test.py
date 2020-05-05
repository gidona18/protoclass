import unittest

import protobj as pt

class Test:
    def test_make(self):
        orenji = pt.make(name='orenji', color='214')
        self.assertEqual(orenji.name == 'orenji')
        self.assertEqual(orenji.color == '214')

        orenji.color = '11'
        self.assertEqual(orenji.color == '11')

    def test_link(self):
        fruit = pt.make(type='fruit')
        orenji = pt.make(name='orenji', color='214')
        orenji = pt.link(orenji, fruit)
        self.assertEqual(orenji.type == 'fruit')


if __name__ == '__main__':
    unittest.main()
