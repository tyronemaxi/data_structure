#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 328.py
Time: 2023/7/13
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        even_head = head.next  # 用来暂存链表
        odd, even = head, even_head

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head  # 拼接

        return head
