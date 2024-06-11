
# Template tes file for bowling
import unittest
from src.bowling import *

class Testbowling(unittest.TestCase):
    def test_bowling(self):
        self.assertEqual(bowling(42), 41, 'The sum is wrong.')