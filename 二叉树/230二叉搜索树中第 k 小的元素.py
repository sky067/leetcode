# -*- coding: utf-8 -*-
# @File    : 230二叉搜索树中第 k 小的元素.py
# @Des     :


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    res = None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return

        # 到达第 k 个元素后，不继续递归
        if self.count >= k:
            return

        self.kthSmallest(root.left, k)

        self.count += 1
        if self.count == k:
            self.res = root.val

        self.kthSmallest(root.right, k)

        return self.res
