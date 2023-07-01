#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: bubble_sort.py
Time: 2023/6/30
"""
"""
冒泡排序
"""


def bubble_sort(arr: [int]):
    if len(arr) <= 1:
        return arr

    n = len(arr)
    for i in range(n):
        is_exchange = False
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_exchange = True

        if not is_exchange:
            break

    return arr


if __name__ == '__main__':
    arr = [10, 2, 3, 19, 2, 10, 100, 2, 222, 190]
    print(bubble_sort(arr))
