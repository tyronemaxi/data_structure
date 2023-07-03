#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: insert_sort.py
Time: 2023/7/1
"""


def insert_sort(arr):
    """
    插入排序
    :param arr:
    :return:
    """
    n = len(arr)
    # if n <= 1:
    #     return arr

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr


if __name__ == '__main__':
   arr = [10, 2, 3, 19, 2, 10, 100, 2, 222, 190]
   print(insert_sort(arr))
