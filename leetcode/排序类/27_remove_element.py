#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 27_remove_element.py
Time: 2023/7/3
"""
# https://leetcode.cn/problems/remove-element/
# 原地排序算法就是特指空间复杂度为 O(1) 的排序算法

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        print(nums[:left])
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([1, 3, 2, 2, 3], 3))
    print(s.removeElement([0,1,2,2,3,0,4,2], 2))


