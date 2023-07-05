#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 75_color_sort.py
Time: 2023/7/4
"""
# https://leetcode.cn/problems/sort-colors/
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[ptr], nums[i] = nums[i], nums[ptr]
                ptr += 1

        for i in range(len(nums)):
            if nums[i] == 1:
                nums[ptr], nums[i] = nums[i], nums[ptr]
                ptr += 1

# 快速排序的子过程 partition
# https://leetcode.cn/problems/sort-colors/solution/kuai-su-pai-xu-partition-guo-cheng-she-ji-xun-huan/
class SolutionTwo:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, index1, index2):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        ptr1 = 0
        ptr2 = len(nums)

        i = 0
        while i < ptr2:
            if nums[i] == 0:
                swap(nums, ptr1, i)
                i += 1
                ptr1 += 1
            elif nums[i] == 1:
                i += 1

            else:
                ptr2 -= 1
                swap(nums, ptr2, i)

        print(nums)


if __name__ == '__main__':
    s = SolutionTwo()
    nums = [1, 2, 2, 1, 0, 0]
    s.sortColors(nums)
