import numpy as np


# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(4) == 5

def test_np():
    assert np.eye(3).sum() ==3.0
