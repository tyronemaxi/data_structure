#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: circle_chain.py
Time: 2023/6/29
"""
from bidirectional_chain import XNode


class CircleChain:
    """
    双向循环链表
    """
    def __init__(self):
        self.head = None

    def add(self, data):
        cur = self.head
        node = XNode(data)
        if cur is None:
            node.next = node
            node.prev = node
            self.head = node
        else:
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
            self.head = node

    def append(self, data):
        cur = self.head
        node = XNode(data)
        if cur is None:
            node.next = node
            node.prev = node
            self.head = node
        else:
            last_node = cur.prev
            node.prev = last_node
            node.next = cur
            cur.prev = node
            last_node.next = node

    def remove_at_end(self):
        cur = self.head
        if cur is None:
            return
        if cur.next == self.head:
            self.head = None
        else:
            last_node = cur.prev
            second_last_node = last_node.prev
            cur.prev = second_last_node
            second_last_node.next = self.head

    def find(self, data):
        pass

    def show_data(self):
        cur = self.head
        print(f"-<{cur.data}>-", end="")  # 头节点多打印一次，表示循环
        while True:
            cur = cur.next
            print(f"-<{cur.data}>-", end="")
            if cur == self.head:
                break

    def __len__(self):
        pass


if __name__ == '__main__':
    chain = CircleChain()
    chain.add(1)
    chain.add(2)
    chain.append(3)
    chain.append(4)
    chain.show_data()
    chain.remove_at_end()
    print()
    chain.show_data()