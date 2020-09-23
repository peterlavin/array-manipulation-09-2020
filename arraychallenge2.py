
from datetime import datetime as dt
import pytest


def array_counts(arr: []) -> []:

    dbl_arr = [[itm, 0] for itm in arr]
        
    for count, item in enumerate(dbl_arr):
        if count == 0:
            continue
        for back_count in range(1, count + 1):  # up to but not including
            if dbl_arr[count - back_count][0] > item[0]:
                item[1] -= abs((item[0] - dbl_arr[count - back_count][0]))
            elif dbl_arr[count - back_count][0] < item[0]:
                item[1] += abs((item[0] - dbl_arr[count - back_count][0]))
    return [item[1] for item in dbl_arr]


class TestArrayChallenge():
    
    def test_array_known_1(self):
        assert array_counts([1, 2, 2, 3]) == [0, 1, 1, 4]
        
    def test_array_known_2(self):
        assert array_counts([2, 4, 3]) == [0, 2, 0]
      
    def test_long_array(self, big_array):
        assert len(array_counts(big_array)) == 1500

    @pytest.mark.parametrize(('a, expected'),
                            [([], []),
                            ([1], [0]),
                            ([1, 2], [0, 1])])
    def test_array_empty(self, a, expected):
        assert array_counts(a) == expected     
   
