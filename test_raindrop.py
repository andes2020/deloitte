import unittest
# from unittest.mock import patch
import unittest.mock
import raindrop as rd

class TestStringMethods(unittest.TestCase):

    def test_invalid_input(self):
        with unittest.mock.patch('builtins.input', return_value='striasdf'):
            with self.assertRaises(ValueError):
                rd.calculate_rain_drop()

    def test_28(self):
        with unittest.mock.patch('builtins.input', return_value='28'):
            self.assertEqual(rd.calculate_rain_drop(), 28)