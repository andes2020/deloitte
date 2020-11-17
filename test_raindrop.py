import unittest
# from unittest.mock import patch
import unittest.mock
import raindrop as rd

class TestStringMethods(unittest.TestCase):

    def test_28(self):
        with unittest.mock.patch('builtins.input', return_value='28'):
            self.assertEqual(rd.calculate_rain_drop(), 'Plong')