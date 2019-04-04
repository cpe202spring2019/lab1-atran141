import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr_1(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    def test_repr_2(self):
    	l = Location('Go', 43.012, 9)
    	self.assertEqual(repr(l), "Location('Go', 43.012, 9)")
    def test_repr_3(self):
    	a = Location('236 Street', 10, 101)
    	self.assertEqual(repr(a), "Location('236 Street', 10, 101)")
    def test_eq_1(self):
    	loc1 = Location("SLO", 35.3, -120.7)
    	loc2 = Location("SLO", 35.3, -120.7)
    	self.assertEqual(loc1, loc2)
    def test_eq_2(self):
    	loc3 = Location("h", 44, 97.2)
    	self.assertEqual(loc3, Location("h", 44, 97.2))
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
