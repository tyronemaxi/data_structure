#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: stack.py
Time: 2023/6/30
"""
from chain.single_chain import SingleChain


class Stack:
    """
    栈的数组实现
    """
    def __init__(self):
        self.__stack = []

    def pull(self):
        """
        出栈
        :return:
        """
        if len(self) > -0:
            item = self.__stack.pop(-1)
            return item
        else:
            return

    def push(self, data):
        """
        入栈
        :return:
        """
        self.__stack.append(data)

    def top(self):
        """
        栈顶
        :return:
        """
        if len(self) > 0:
            return self.__stack[-1]
        else:
            return

    def __len__(self):
        """
        长度
        :return:
        """
        return len(self.__stack)


class ChainStack:
    """
    基于链表实现栈
    """
    def __init__(self):
        self.__stack: SingleChain = None

    def pull(self):
        """
        出栈
        :return:
        """
        return self.__stack.delete_head()

    def push(self, data):
        """
        入栈
        :return:
        """
        if self.__stack is None:
            s = SingleChain()
            s.add(data)
            self.__stack = s
        else:
            self.__stack.add(data)

    def top(self):
        """
        栈顶
        :return:
        """
        cur = self.__stack.get_head()
        return cur.data

    def __len__(self):
        """
        长度
        :return:
        """
        if self.__stack is None:
            return 0
        return len(self.__stack)


if __name__ == '__main__':
    # stack = Stack()
    stack = ChainStack()
    print(len(stack))

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.top())
    print(stack.pull())
    print(stack.pull())
    print(stack.pull())
    print(stack.top())
