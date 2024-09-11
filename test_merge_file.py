"""Test cases for the merge_sort function from hw2_debugging module."""

from hw2_debugging import merge_sort

def test_sorted():
    """Test already sorted arrays"""
    sorted_array = [1, 2, 3, 4, 5, 6]
    res = merge_sort(sorted_array)
    assert res == sorted_array, f"Expected [1, 2, 3, 4, 5, 6] but got {res}"

def test_sorted2():
    """Sorts an array"""
    array = [3, 1, 6, 5, 4, 2]
    sorted_array = [1, 2, 3, 4, 5, 6]
    res = merge_sort(array)
    assert res == sorted_array, f"Expected [1, 2, 3, 4, 5, 6] but got {res}"