#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: bidirectional_chain.py
Time: 2023/6/29
"""


class XNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class BidirectionalChain:
    """
    双向链表
    : history(data, index) 查找记录，便于判断向前，或者向后查找，优化查找效率
    """
    def __init__(self):
        self.head = None
        self.history = None

    def add(self, data):
        """
        头部插入数据
        :return:
        """
        cur = self.head
        node = XNode(data)
        if cur is None:
            self.head = node
        else:
            node.next = cur
            cur.prev = node
            self.head = node

    def append(self, data):
        """
        尾部插入数据
        :return:
        """
        cur = self.head
        node = XNode(data)
        while cur.next:
            cur = cur.next

        cur.next = node
        node.prev = cur

    def find(self, data):
        """
        查找数据 O(log(n))
        :param data:
        :return:
        """
        cur = self.history
        flag = False
        history = None
        if cur:
            if data == cur.data:
                history = cur
                flag = True
            elif data < cur.data:
                # 向前查找
                while cur:
                    if cur.data == data:
                        flag = True
                        history = cur
                    cur = cur.prev
            else:
                # 向后查找
                while cur:
                    if cur.data == data:
                        flag = True
                        history = cur
                    cur = cur.next
        else:
            cur = self.head
            while cur:
                if cur.data == data:
                    flag = True
                    history = cur
                cur = cur.next

        self.history = history
        return flag

    def insert(self, data, index: int):
        """
        插入一个数据
        :param data:
        :param index:
        :return:
        """
        length = len(self)
        cur = self.head
        node = XNode(data)

        if 0 <= index <= length:
            while index > 1:  # O（n）
                cur = cur.next
                index -= 1

            _next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node
            node.next = _next

        elif index < 0:
            self.add(data)
        else:
            self.append(data)

    def remove(self, data):
        cur = self.head
        _pre = None
        while cur:
            if data == cur.data:
                if cur == self.head:
                    self.head = self.head.next  # 链表头节点需要特殊关注
                    return
                _pre.next = cur.next
                if cur.next is None:  # 尾部节点删除时 None 值判断
                    return
                else:
                    cur.next.prev = _pre
            _pre = cur
            cur = cur.next

        return

    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            cur = cur.next
            count += 1

        return count

    def show_data(self):
        cur = self.head
        while cur:
            print(f"-<{cur.data}>-", end="")
            cur = cur.next


if __name__ == '__main__':
    chain = BidirectionalChain()
    chain.add(1)
    chain.append(2)
    chain.add(0)
    chain.insert(1, 1)
    chain.show_data()
    print()
    print(chain.find(2))
    print(chain.find(0))
    print(chain.history.data)
    chain.remove(1)
    chain.remove(2)
    chain.remove(1)
    chain.show_data()

