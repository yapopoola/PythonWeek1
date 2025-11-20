'''def basic_test_cases():
        test.assert_equals(positive_sum([1,2,3,4,5]),15)
        test.assert_equals(positive_sum([1,-2,3,4,5]),13)
        test.assert_equals(positive_sum([-1,2,3,4,-5]),9)'''

import pytest
from person import positive_sum

def test_sum_of_all_positive_nums1():
    sum_of_all = positive_sum([1,2,-3])
    assert sum_of_all == 3

def test_sum_of_all_positive_nums2():
    sum_of_all = positive_sum([1,2,3,-4])
    assert sum_of_all == 6

def test_sum_of_all_positive_nums3():
    sum_of_all = positive_sum([1,2,3,4,-5])
    assert sum_of_all == 10

def test_sum_of_all_positive_nums4():
    sum_of_all = positive_sum([1,2,3,4,5,6,-7])
    assert sum_of_all == 21

def test_sum_of_all_positive_nums5():
    assert positive_sum([1,2,3,4,5,6,7,-8]) == 28

def test_for_errors():
    with pytest.raises(TypeError):
        positive_sum([1,2,3,4,5,"six"])


