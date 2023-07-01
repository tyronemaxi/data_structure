#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: quick_sort.py
Time: 2023/7/1
"""


def quick_sort(arr):
    """
    快速排序
    :param arr:
    :return:
    """
    n = len(arr)
    if n <= 1:
        return arr

    mid = arr[0]
    left = [i for i in arr[1:] if i <= mid]
    right = [i for i in arr[1:] if i > mid]

    return quick_sort(left) + [mid] + quick_sort(right)


if __name__ == '__main__':
    arr = [10, 2, 3, 19, 2, 10, 100, 2, 222, 190]
    print(quick_sort(arr))

