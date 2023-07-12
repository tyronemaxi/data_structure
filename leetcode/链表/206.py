#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 206.py
Time: 2023/7/12
"""
# https://leetcode.cn/problems/reverse-linked-list/

from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res, p = None, head
        while p:
            res, res.next, p = p, res, p.next

        return res
