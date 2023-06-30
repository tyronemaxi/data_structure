#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: stack.py
Time: 2023/6/30
"""

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


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.top())
    print(stack.pull())
    print(stack.pull())
    print(stack.pull())
    print(stack.top())
