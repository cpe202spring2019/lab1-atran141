import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):
    def test_max_list_iter_1(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
    def test_max_list_iter_2(self):
        lst = [10,1,2,6,7,9.94,99,13.66,-106]
        self.assertEqual(max_list_iter(lst), 99)
    def test_max_list_iter_3(self):
        lst = [54,864561,6513,48,843,0,0.21,64]
        self.assertEqual(max_list_iter(lst), 864561)
    def test_max_list_iter_4(self):
        lst = [-516,6.000003,-164,-4894,-87,-6.664]
        self.assertEqual(max_list_iter(lst), 6.000003)
    def test_max_list_iter_5(self):
        lst = [8,8,8]
        self.assertEqual(max_list_iter(lst), 8)
    def test_max_list_iter_6(self):
        lst = [6,7,7,1]
        self.assertEqual(max_list_iter(lst), 7)
    def test_max_list_iter_7(self):
        lst = [8,8,8,9,9,9]
        self.assertEqual(max_list_iter(lst), 9)
    def test_max_list_iter_8(self):
        lst = []
        self.assertEqual(max_list_iter(lst), None)
    def test_max_list_iter_9(self):
        lst = [-5.0554]
        self.assertEqual(max_list_iter(lst), -5.0554)

    def test_reverse_rec_1(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
    def test_reverse_rec_2(self):
        self.assertEqual(reverse_rec([100,0,100,0]),[0,100,0,100])
    def test_reverse_rec_3(self):
        self.assertEqual(reverse_rec([3.667]),[3.667])
    def test_reverse_rec_4(self):
        self.assertNotEqual(reverse_rec([1,2,3]),[1,2,3])
    def test_reverse_rec_5(self):
        self.assertEqual(reverse_rec([-560,1000,647]),[647,1000,-560])
    def test_reverse_rec_6(self):
        self.assertEqual(reverse_rec([]),[])

    def test_bin_search_1(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
    def test_bin_search_2(self):
        list_val =[0,1]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), None)
    def test_bin_search_3(self):
        list_val =[31,310,654,3102,4885,8687,61231]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(654, 0, len(list_val)-1, list_val), 2)
    def test_bin_search_4(self):
        list_val =[-64,-49.6,0,12,18,99,112,126,4750,10000]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(99, 0, len(list_val)-1, list_val), 5)
    def test_bin_search_5(self):
        list_val =[0,1,2,3]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(2, 0, len(list_val)-1, list_val), 2)
    def test_bin_search_6(self):
        list_val =[0,1,2,3,64,85]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1)
    def test_bin_search_7(self):
        list_val =[0,1,2,3,64,85]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0)
    def test_bin_search_8(self):
        list_val =[0,1,2,3,64,85]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(85, 0, len(list_val)-1, list_val), 5)

if __name__ == "__main__":
        unittest.main()

    
