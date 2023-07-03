#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 148_sort_chain.py
Time: 2023/7/1
"""
from typing import Optional


class ListNode:
    def __init__(self, val=100000):
        self.val = val
        self.next = None


class Solution:
        def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
           # 递归终止条件
            if not head or not head.next:
                return head
            # 快慢指针查找中节点
            pre, slow, fast = None, head, head
            while fast and fast.next:
                pre, slow, fast = slow, slow.next, fast.next.next

            pre.next = None  # 断开
            return self.merge(self.sortList(head), self.sortList(slow))

        def merge(self, h1, h2):
            dummy = ListNode()
            cur = dummy
            while h1 and h2:
                if h1.val <= h2.val:
                    cur.next = h1
                    h1 = h1.next
                    # tail.next, tail, h1 = h1, h1, h1.next

                else:
                    cur.next = h2
                    h2 = h2.next
                    # tail.next, tail, h2 = h2, h2, h2.next
                cur = cur.next

            cur.next = h1 or h2
            return dummy.next


if __name__ == '__main__':
    head = None
    arr = [9, 10, 1, 2, -1, 0]
    for i in arr:
        node = ListNode(i)
        if head is None:
            head = node
        else:
            cur = head
            while cur.next:
                cur = cur.next

            cur.next = node

    cur = head
    while cur:
        print(f"<{cur.val}>-", end="")
        cur = cur.next

    s = Solution()

    print()
    new_head = s.sortList(head)
    cur = new_head
    while cur:
        print(f"<{cur.val}>-", end="")
        cur = cur.next
