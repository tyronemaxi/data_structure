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
        sorted = []
        p1, p2 = 0, 0
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

        print(sorted)
        nums1[:] = sorted

"""
    总结：这一题合并两个有序数组，其特殊性在于 nums1 中是用 0 替代了部分空白（个人感觉多此一举），于是在进行 if-elif-else 判断时，优先级要进行调整，比如
    p1 == m ,p2 == n 要优先判断，否则 0 值会干扰结果。
"""

if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    s.merge(nums1, 3, nums2, 3)
