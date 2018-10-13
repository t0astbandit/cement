#!/usr/bin/python3

import unittest

class TestStringMethods(unittest.TestCase):

    def test_float(self):
        self.assertFalse(1.4.is_integer())

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()