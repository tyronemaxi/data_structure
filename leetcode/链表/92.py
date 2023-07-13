#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 92.py
Time: 2023/7/13
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(head):
            res, p = None, head

            while p:
                res, res.next, p = p, res, p.next


        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node

        # 指针到左边的前一个节点
        for _ in range(left - 1):
            pre = pre.next


        right_node = pre
        for _ in range(right-left+1):
            right_node = right_node.next

        # 切断子链表
        mid_node = pre.next
        curr = right_node.next  # 后置节点

        pre.next = None
        right_node.next = None

        reverse(mid_node)

        pre.next = right_node  # 这里可能不好理解，是因为反转后尾节点变成了头节点
        mid_node.next = curr   # 连接后置节点

        return dummy_node.next


# 第二种解法，一次遍历，实现反转链表（头插法）

def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy

    for _ in range(left-1):
        pre = pre.next

    cur = pre.next
    for _ in range(right-left):
        next = cur.next
        cur.next = next.next
        next.next = pre.next
        pre.next = next

    return dummy.next
