#!/usr/bin/env python
# coding: utf-8

import unittest
import sqlite3
from simplemapper import BaseMapper

class TestORClass(BaseMapper):
    rows = (('num', 'int'), ('body', 'text'))
class TestSimpleMapper(unittest.TestCase):

    def testNoTable(self):
        with self.assertRaises(sqlite3.OperationalError):
            actual = TestORClass.select()
            print actual

    def testCreateTable(self):
        TestORClass.createtable()
        actual = len([x for x in TestORClass.select()])
        self.assertEqual(0, actual)


if __name__ == '__main__':
    unittest.main()


