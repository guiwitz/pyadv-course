from pyadv_course import algos
import numpy as np

def test_add_one():
    
    x = 1
    out = algos.add_one(x)
    assert out == 2

def test_add_one_list():

    x = [1,2,3]
    out = algos.add_one(x)
    np.testing.assert_array_equal(out, [2,3,4])

