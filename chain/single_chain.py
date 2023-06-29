#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: single_chain.py
Time: 2023/6/29
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleChain(object):
    """
    单链表
    """
    def __init__(self):
        self.head = None

    def insert(self, data, index: int):
        """
        插入一个数据
        :param data:
        :param index:
        :return:
        """
        length = len(self)
        cur = self.head
        node = Node(data)

        if 0 <= index <= length:
            while index > 1:  # O（n）
                cur = cur.next
                index -= 1

            _next = cur.next
            node.next = _next
            cur.next = node

        elif index < 0:
            self.add(data)
        else:
            self.append(data)

    def add(self, data):
        """
        头部插入数据
        :return:
        """
        cur = self.head
        node = Node(data)
        if cur is None:
            self.head = node
        else:
            node.next = cur
            self.head = node

    def append(self, data):
        """
        尾部插入数据
        :return:
        """
        cur = self.head
        node = Node(data)
        while cur.next:
            cur = cur.next

        cur.next = node

    def find(self, data):
        cur = self.head
        index = 0
        while cur:
            if data == cur.data:
                return index
            cur = cur.next
            index += 1

        return None

    def remove(self, data):
        """
        删除数据，默认删除第一个
        :param data:
        :return:
        """
        cur = self.head
        _pre = None
        while cur:
            if data == cur.data:
                if cur == self.head:
                    self.head = self.head.next  # 链表头节点需要特殊关注
                    return
                _pre.next = cur.next
            _pre = cur
            cur = cur.next

        return None

    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            cur = cur.next
            count += 1

        return count

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next

    def show_data(self):
        cur = self.head
        while cur:
            print(f"-<{cur.data}>-", end="")
            cur = cur.next


if __name__ == '__main__':
    chain = SingleChain()
    chain.add(1)
    chain.append(2)
    chain.append(3)
    chain.append(4)
    chain.insert(5, 2)
    chain.insert(-1, -1)
    chain.insert(100, 100)
    chain.insert(1000, 1)
    chain.show_data()
    print()

    for i in chain:
        print(i)

    print(chain.find(-1))
    print(chain.find(1))
    print(chain.find(100))
    chain.remove(1000)
    chain.remove(100)
    chain.remove(4)
    chain.show_data()
