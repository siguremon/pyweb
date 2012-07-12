#!/usr/bin/env python
# coding: utf-8

import unittest
import mock
import re
from simpletemplate import SimpleTemplate, if_pat, endif_pat, for_pat, endfor_pat, value_pat

class TestSample(unittest.TestCase):
    def test_if_pat_is_not_match(self):
        actual = if_pat.search('$if:')
        self.assertIsNone(actual)

    def test_if_pat_is_match(self):
        actual = if_pat.search('$if True:')
        self.assertIsNotNone(actual)
        self.assertEqual('True:', actual.group(1))

    def test_endif_pat_is_not_match(self):
        actual = endif_pat.search('$end')
        self.assertIsNone(actual)

    def test_endif_pat_is_match(self):
        actual = endif_pat.search('$endif')
        self.assertIsNotNone(actual)

    def test_for_pat_is_not_match(self):
        actual = for_pat.search('$for in ')
        self.assertIsNone(actual)

    def test_for_pat_is_match(self):
        actual = for_pat.search('$for i in items:')
        self.assertIsNotNone(actual)
        self.assertEqual('i', actual.group(1))
        self.assertEqual('items:', actual.group(2))

    def test_value_pat_is_not_match(self):
        actual = value_pat.search('$')
        self.assertIsNone(actual)

    def test_value_pat_is_match(self):
        actual = value_pat.search('${value}')
        self.assertIsNotNone(actual)

        self.assertEqual('value', actual.group(1))
        
    def test_handle_value(self):
        t = SimpleTemplate('${value}')
        m = value_pat.search(t.lines[0])
        self.assertIsNotNone(m)
        dict = {'value':'actual'}
        cur, o = t.handle_value(m, 0, dict)
        self.assertEqual(0, cur)
        self.assertEqual('actual\n', o)

    def test_handle_value2(self):
        dic = {'value':'actual'}
        t = SimpleTemplate('${value}value')
        m = value_pat.search(t.lines[0])
        self.assertIsNotNone(m)
        cur, o = t.handle_value(m, 0, dic)
        self.assertEqual(0, cur)
        self.assertEqual('actualvalue\n', o)

    def test_process2(self):
        t = SimpleTemplate("""
$if True:
    test
$endif
""")
        body = t.render({})
        self.assertEqual("""
    test

""", body)
        
    def test_process(self):
        with mock.patch('simpletemplate.SimpleTemplate.process') as m:
            m.return_value = [0, '']
            t = SimpleTemplate('value')

            o = t.render()
            self.assertEqual(m.call_count, 1)
            self.assertEqual('', o)
        
if __name__ == '__main__':
    unittest.main()
