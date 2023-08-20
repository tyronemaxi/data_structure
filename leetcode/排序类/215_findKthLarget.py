#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 215_findKthLarget.py
Time: 2023/7/10
"""
import random
# https://leetcode.cn/problems/kth-largest-element-in-an-array/
# 解题参考：https://www.bilibili.com/video/BV1A5411H7zr/?spm_id_from=333.337.search-card.all.click&vd_source=67c3c7f430d599a6b5dacd9127487fc7
from typing import List

# 快排 partition
class Solution:
    def findKthLargest(self, nums: List[int], k: int):
        return self.quick_sort(nums, 0, len(nums) - 1, k)

    def quick_sort(self, nums, l, r, k):
        index = self.random_pivot(nums, l, r)
        if index == k - 1:
            return nums[index]

        elif index > k - 1:
            return self.quick_sort(nums, l, index - 1, k)

        else:
            return self.quick_sort(nums, index + 1, r, k)

    def random_pivot(self, nums, l, r):
        i = random.randint(l, r)
        nums[i], nums[r] = nums[r], nums[i]
        return self.partition(nums, l, r)

    def partition(self, nums, l, r):
        pivot = nums[r]
        right = r
        while l <= r:
            while l <= r and nums[l] > pivot:
                l += 1

            while l <= r and nums[r] <= pivot:
                r -= 1

            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]

        nums[l], nums[right] = nums[right], nums[l]

        return l

# 堆
from heapq import heapify, heappush, heappop

class Solution2:
    def findKthLargest(self, nums: List[int], k: int):
        min_heap = []
        heapify(min_heap)
        for num in nums:
            heappush(min_heap, num)
            if len(min_heap) > k:
                heappop(min_heap)
        return min_heap[0]


if __name__ == '__main__':
    nums = [10, 2, 1, 3, 1]
    s = Solution2()
    print(s.findKthLargest(nums, 2))
