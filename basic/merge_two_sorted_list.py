#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: merge_two_sorted_list.py
Time: 2023/8/12
"""
# 合并两个有序数组
import random


def merge_list(arr1: list, arr2: list):
    """
    :param arr1:
    :param arr2:
    :return:
    """
    li = []
    while arr1 and arr2:
        value1, value2 = arr1[-1], arr2[-1]
        if value1 >= value2:
            li.append(arr1.pop(-1))
        else:
            li.append(arr2.pop(-1))

    while arr1:
        li.append(arr1.pop(-1))

    while arr2:
        li.append(arr2.pop(-1))

    return li


def merge_list_2(arr1: list, arr2: list):
    """
    不使用额外空间, 借助插入排序
    :param arr1:
    :param arr2:
    :return:
    """
    arr1.extend(arr2)
    n = len(arr1)
    for i in range(1, n):
        value = arr1[i]
        j = i-1
        while j >= 0 and arr1[j] > value:
            arr1[j+1] = arr1[j]
            j -= 1

        arr1[j+1] = value

    return arr1


if __name__ == '__main__':
    array1 = [1, 2, 3, 4, 5, 6, 7, 8]
    array2 = [1, 2, 12, 13, 14, 15]

    print(merge_list_2(array1, array2))
    print(merge_list(array1, array2))
