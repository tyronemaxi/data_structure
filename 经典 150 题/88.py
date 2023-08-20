#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 88.py
Time: 2023/8/20
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = 0, 0
        sorted = []
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1

        nums1[:] = sorted
        print(nums1)


if __name__ == '__main__':
    s = Solution()
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 3, 4, 5, 6]
    s.merge(num1, len(num1), num2, len(num2))

