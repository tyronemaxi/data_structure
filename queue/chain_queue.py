#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: chain_queue.py
Time: 2023/6/30
"""
from chain.single_chain import Node


class ChainQueue:
    def __init__(self):
        self._head = None
        self._tail = None

    def enqueue(self, data):
        node = Node(data)
        if self._tail:
            self._tail.next = node
        else:
            self._head = node

        self._tail = node

    def dequeue(self):
        if self._head:
            value = self._head.data
            self._head = self._head.next
            if not self._head:
                self._tail = None
            return value



