# -*- coding: utf-8 -*-
# @File    : 543二叉树的直径.py
# @Des     :


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 二叉树深度的变种
        route = 0

        def dfs(root):
            nonlocal route

            if not root:
                return -1  # 求边，最后一个节点不计算
            left_dep = dfs(root.left) + 1

            right_dep = dfs(root.right) + 1

            route = max(route, left_dep + right_dep)
            return max(left_dep, right_dep)

        dfs(root)
        return route