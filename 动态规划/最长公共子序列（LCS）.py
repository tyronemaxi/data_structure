#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: tyrone
File: 最长公共子序列（LCS）.py
Time: 2023/8/3
"""
#  leetcode 题地址：https://leetcode.cn/problems/longest-common-subsequence/solutions/696763/zui-chang-gong-gong-zi-xu-lie-by-leetcod-y7u0/
# 讲解的很清楚：https://www.bilibili.com/video/BV1ey4y1d7oD/?spm_id_from=333.337.search-card.all.click&vd_source=67c3c7f430d599a6b5dacd9127487fc7
"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

 

示例 1：

输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace" ，它的长度为 3 。
示例 2：

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。
示例 3：

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。
 

提示：

1 <= text1.length, text2.length <= 1000
text1 和 text2 仅由小写英文字符组成。
"""
import numpy as np


def max_long_common_subquence(s1: str, s2: str):
    """
    :param s1:
    :param s2:
    :return:
    """
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[m][n]


if __name__ == '__main__':
    s1 = "ABCBDAB"
    s2 = "BDCABC"

    print(max_long_common_subquence(s1, s2))


