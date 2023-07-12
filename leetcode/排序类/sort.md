#排序
- 148 
- 56
- 27
- 179
- 75
- 215
- 4
总结：快慢指针和反转链表是基础
# leet code 215
> 数组中第 K 个最大元素
## 题目描述
https://leetcode.cn/problems/kth-largest-element-in-an-array/

## 解题思路
### 暴力法
- 使用内置排序函数 `sort()` 从小到大
- 返回倒数第 k 个元素：returns nums[len(nums) - k]
### 快速排序的 partition
- 取随机 pivot 基准值
- 分区 partition, 大｜pivot|小
- 返回第 k 大的元素
### 堆
- 堆是一个完全二叉树
- 堆中的每一个节点的值都必须大于等于（或小于等于）其子树中每个节点的值

