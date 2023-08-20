#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 4.py
Time: 2023/8/18
"""
from typing import List


# https://leetcode.cn/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 排序
        num = []
        while nums1 and nums2:
            a = nums1[0]
            b = nums2[0]
            if a < b:
                num.append(nums1.pop(0))
            else:
                num.append(nums2.pop(0))
        while nums1:
            num.append(nums1.pop(0))

        while nums2:
            num.append(nums2.pop(0))

        print(num)
        n = len(num)

        if n % 2 == 1:
            mid = num[n // 2]
        else:
            mid_index = n // 2
            mid = (num[mid_index-1] + num[mid_index]) / 2

        return mid


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 5]
    nums2 = [1, 2, 3, 4]
    print(s.findMedianSortedArrays(nums, nums2))
