"""
This module implements merge sort.
"""

import rand


def merge_sort(array):
    """Performs merge sort on the input array"""
    if len(array) == 1:
        return array

    half = len(array) // 2

    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))


def recombine(left_arr, right_arr):
    """Merges two sorted arrays into one"""
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    merge_index = 0
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[merge_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[merge_index] = right_arr[right_index]
            right_index += 1
        merge_index += 1

    while left_index < len(left_arr):
        merge_arr[merge_index] = left_arr[left_index]
        left_index += 1
        merge_index += 1

    while right_index < len(right_arr):
        merge_arr[merge_index] = right_arr[right_index]
        right_index += 1
        merge_index += 1

    return merge_arr


arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
