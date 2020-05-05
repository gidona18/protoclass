import unittest

import protobj as pt

class Test(unittest.TestCase):
    def test_make(self):
        # basic creation
        orenji = pt.make(name='orenji', color='214')
        self.assertEqual(orenji.name, 'orenji')
        self.assertEqual(orenji.color, '214')
        # basic mutation
        orenji.color = '11'
        self.assertEqual(orenji.color, '11')

    def test_link(self):
        # check basic propagation
        fruit = pt.make(type='fruit')
        orenji = pt.make(name='orenji', color='214')
        orenji = pt.link(orenji, fruit)
        self.assertEqual(orenji.type, 'fruit')
        # assert that changes in children do not propagate to parents
        orenji.type = 'ORENJI!!!'
        self.assertEqual(orenji.type, 'ORENJI!!!')
        self.assertEqual(fruit.type, 'fruit')
        # assert that propagation works after instantiation
        fruit.jp = 'フルーツ'
        self.assertEqual(fruit.jp, 'フルーツ')
        self.assertEqual(orenji.jp, 'フルーツ')
        # and once again, parents should be unaffected by children
        orenji.jp = 'オレンジ'
        self.assertEqual(orenji.jp, 'オレンジ')
        self.assertEqual(fruit.jp, 'フルーツ')
        # let's test a third generation
        akai_orenji = pt.link(pt.make(color='9'), orenji)
        self.assertEqual(akai_orenji.color, '9')
        self.assertEqual(akai_orenji.type, 'ORENJI!!!')
        self.assertEqual(akai_orenji.jp, 'オレンジ')
        self.assertEqual(orenji.jp, 'オレンジ')
        self.assertEqual(fruit.jp, 'フルーツ')


if __name__ == '__main__':
    unittest.main()
