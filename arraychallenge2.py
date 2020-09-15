'''
Created on 12 Sep 2020

@author: peter
'''

import unittest

def calc_array(arr: list) -> list:
    
    dbl_arr = [[item,0] for item in arr]

    for count, item in enumerate(dbl_arr):
        if count == 0:
            continue
        for back_count in range(1,count+1):
            item[1] += abs(item[0] - dbl_arr[count - back_count][0])
            
    return [item[1] for item in dbl_arr]

def ret_val(val):
    return val*2

class TestCalcArray(unittest.TestCase):
    
    def test1(self):
        """ Increasing and equal only, example from test """
        self.assertEqual(calc_array([1,2,2,3]),[0,1,1,4])

    def test2(self):
        """ Increasing and decreasing """  
        self.assertEqual(calc_array([1,2,5,3]),[0,1,7,5])
        
    def test3(self):
        self.assertEqual(calc_array([1,12,5,3,5]),[0,11,11,13,13])
        
    def test4(self):
        """Len of 2, decreasing"""
        self.assertEqual(calc_array([5,3]),[0,2])
        
    def test5(self):
        """One element list"""
        self.assertEqual(calc_array([1]),[0])
        
    def test6(self):
        """Zero element list"""
        self.assertEqual(calc_array([]),[])

if __name__ == '__main__':
    unittest.main(verbosity = 2)

    
