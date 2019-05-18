import unittest
import random

from main import find_percent_proportion, increasing_number, decreasing_number, convert_integer_to_list

class BouncyNumberTestCase(unittest.TestCase):
    def test_fifty_percent_proportion(self):
        self.assertEqual(find_percent_proportion(50)[0], 538)

    def test_ninety_percent_proportion(self):
        self.assertEqual(find_percent_proportion(90)[0], 21780)

    def test_increasing_number(self):
        self.assertTrue(increasing_number(convert_integer_to_list(1169)))
        self.assertFalse(increasing_number(convert_integer_to_list(98498)))

    def test_decreasing_number(self):
        self.assertTrue(decreasing_number(convert_integer_to_list(9933)))
        self.assertFalse(decreasing_number(convert_integer_to_list(76326)))

    def test_convert_in_to_list(self):
        self.assertEqual(list, type(convert_integer_to_list(45435)))

    def test_types_convert_in_to_list(self):
        self.assertRaises(TypeError, convert_integer_to_list, 'dsfsf')

    def test_values_increasing_number(self):
        self.assertRaises(ValueError, convert_integer_to_list, -19293)
