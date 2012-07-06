# coding: utf-8

import unittest

class TestSample(unittest.TestCase):
    def setUp(self):
        pass

    def testlist1(self):
        actual = [1, 2, 3, 4, 5]
        self.assertEqual(1, actual[0])
        self.assertListEqual([1, 2, 3, 4, 5], actual)

    def testlist2(self):
        actual = [1, 2, 3, 4, 5]
        actual[2] = 'change'
        self.assertEqual('change', actual[2])

    def testtuple(self):
        actual = (1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            tuple[2] = 'change'

    def testdictionary(self):
        actual = {'a': 1, 'b': 'text', 'c' : 100}
        self.assertEqual('text', actual['b'])

if __name__ == '__main__':
    unittest.main()
