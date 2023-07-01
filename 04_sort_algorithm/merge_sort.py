#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: merge_sort.py
Time: 2023/7/1
"""


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))

    while right:
        result.append(right.pop(0))

    del left
    del right
    return result


def merge_sort(arr):
    """
    归并排序
    """
    n = len(arr)
    if n <= 1:
        return arr

    middle = n // 2
    left, right = arr[0:middle], arr[middle:]

    return merge(merge_sort(left), merge_sort(right))


if __name__ == '__main__':
    arr = [10, 2, 3, 19, 2, 10, 100, 2, 222, 190]
    print(merge_sort(arr))
