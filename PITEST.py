# test suite
import unittest
import math as math
from calculatepi import calculatepi

class PITEST(unittest.TestCase):
    # negative test function to test if values are almost equal with place
    def testifpisareequal(self):
        calculated = calculatepi()
        self.assertAlmostEqual(calculated, math.pi)