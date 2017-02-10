import numpy as np
import pandas as pd

# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(4) == 5

def test_np():
    assert np.eye(3).sum() ==3.0

def test_pandas():
    df = pd.read_csv('MOCK_DATA.csv')
    assert len(df) == 1000

if __name__ == '__main__':
    test_pandas()
