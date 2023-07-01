#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: chose_sort.py
Time: 2023/7/1
"""


def choose_sort(arr):
    """
    选择排序
    :param arr:
    :return:
    """
    n = len(arr)
    if n <= 1:
        return arr

    for i in range(n):
        for j in range(i, n):
            if arr[j] < arr[i]:
                min_index = j
                arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == '__main__':
   arr = [2, 1, 1, 19, 2, 10, 100, 2, 222, 190]
   print(choose_sort(arr))
