import pytest
from hw2_debugging import merge_sort

def test_sorted():
    """Test already sorted arrays"""
    sorted_array = [1, 2, 3, 4, 5, 6]
    res = merge_sort(sorted_array)
    assert res == sorted_array, f"Expected [1, 2, 3, 4, 5, 6] but got {res}"