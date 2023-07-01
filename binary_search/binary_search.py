#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: binary_search.py
Time: 2023/7/1
"""


def binary_search(arr: list, target: int):
    """
    二分查找
    :param arr:
    :param target:
    :return:
    """
    low, high = 0, len(arr)
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1


def binary_search_recursion(arr: list, target: int):
    """
    二分查找递归实现
    :param arr:
    :param target:
    :return:
    """
    pass


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 10, 18, 19, 20]
    print(binary_search(arr, 10))
