import random

from unittest import TestCase, mock

from main import find_percent_proportion, increasing_number, decreasing_number
from main import convert_integer_to_list, bouncy_number, proportion_bouncy_numbers

class BouncyNumberTestCase(TestCase):
    def test_find_percent_proportion(self):
        self.assertEqual(tuple, type(find_percent_proportion(10)))

    def test_fifty_find_percent_proportion(self):
        self.assertEqual(find_percent_proportion(50)[0], 538)

    def test_ninety_find_percent_proportion(self):
        self.assertEqual(find_percent_proportion(90)[0], 21780)

    def test_increasing_number(self):
        self.assertTrue(increasing_number(convert_integer_to_list(1169)))
        self.assertFalse(increasing_number(convert_integer_to_list(98498)))

    def test_decreasing_number(self):
        self.assertTrue(decreasing_number(convert_integer_to_list(9933)))
        self.assertFalse(decreasing_number(convert_integer_to_list(76326)))

    @mock.patch('main.decreasing_number', autospec=True)
    @mock.patch('main.increasing_number', autospec=True)
    def test_bouncy_number(self, mock_increasing_number, mock_decreasing_number):
        mock_increasing_number.return_value = False
        mock_decreasing_number.return_value = False

        self.assertTrue(bouncy_number([1, 4, 5]))
        self.assertTrue(mock_increasing_number.called)
        self.assertTrue(mock_decreasing_number.called)

        mock_increasing_number.return_value = True

        self.assertFalse(bouncy_number([1, 4, 5]))
        self.assertTrue(mock_increasing_number.called)

    def test_convert_integer_to_list(self):
        self.assertEqual(list, type(convert_integer_to_list(45435)))

    def test_types_convert_integer_to_list(self):
        self.assertRaises(TypeError, convert_integer_to_list, 'dsfsf')

    def test_values_convert_integer_to_list(self):
        self.assertRaises(ValueError, convert_integer_to_list, -19293)

    def test_proportion_bouncy_numbers(self):
        self.assertEqual(10, proportion_bouncy_numbers(100, 10))

    def test_values_proportion_bouncy_numbers(self):
        self.assertRaises(ValueError, proportion_bouncy_numbers, 0, 100)
        self.assertRaises(ValueError, proportion_bouncy_numbers, 10, 100)
