#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 5.py
Time: 2023/8/18
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = len(s) * [0]
        if not s:
            return s


    def judge(s: str):
        flag = False
        if s[::-1] == s:
           flag = True

        return flag


if __name__ == '__main__':
    s = "aba"
    print(judge(s))
