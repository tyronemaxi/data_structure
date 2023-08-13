#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: Longest Increasing Subsequence.py
Time: 2023/8/13
"""
# 最长递增子序列
# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/


def LIS(arr: list):
    n = len(arr)

    if n == 0:
        return 0

    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]

    print(dp)
    return max(dp)


if __name__ == '__main__':
    arr = [3, 10, 2, 1, 20]
    print(LIS(arr))
    arr = []
    print(LIS(arr))
    arr = [1, 2, 3, 2, 3, 2, 1]
    print(LIS(arr))