
# Template tes file for FizzBuzz
import unittest
from src.fizzBuzz import *

class TestfizzBuzz(unittest.TestCase):
    def test_fizzBuzz(self):
        self.assertEqual(fizzBuzz(42), 41, 'The sum is wrong.')