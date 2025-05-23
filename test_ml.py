import pytest
import os
import pandas as pd
from ml.data import apply_label


# TODO: implement the first test. Change the function name and input as needed
def test_apply_label():
    """
    tests the operation of apply_label() function in data.py
    """
    assert apply_label([1]) == ">50K"
    assert apply_label([0]) == "<=50K"

    
# TODO: implement the second test. Change the function name and input as needed
def test_slice_output_file_exists():
    """
    test the existence of 'slice_output.txt' in the current directory
    """
    slice_output_path = os.path.join(os.getcwd(), 'slice_output.txt')
    assert os.path.exists(slice_output_path)


# TODO: implement the third test. Change the function name and input as needed
def test_metrics_range():
    """
    checks slice output
    verifies value of each metric (precision, recall, f-score)
    is between 0.0 & 1 (inclusive)
    """
    df = pd.read_csv('data/slice_output.csv')
    assert df['precision'].between(0,1).all()
    assert df['recall'].between(0,1).all()
    assert df['f1'].between(0,1).all()
    

