from pyadv_course import algos
import numpy as np
import pytest

def test_add_one():
    
    x = 1
    out = algos.add_one(x)
    assert out == 2

def test_add_one_list():

    x = [1,2,3]
    out = algos.add_one(x)
    np.testing.assert_array_equal(out, [2,3,4])

@pytest.mark.parametrize("test_input, expected", 
                         [([1, 2], [2, 3]), ([1.1, 2.2], [2.1, 3.2])])
def test_add_multiple(test_input, expected):

    out = algos.add_one(test_input)
    np.testing.assert_array_equal(out, expected)


