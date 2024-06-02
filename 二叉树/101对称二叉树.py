# -*- coding: utf-8 -*-
# @File    : 101对称二叉树.py
# @Des     :




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
相等二叉树的变种
难度：simple
"""
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_sample_tree(left, right):
            # 收否都为空
            if left is None or right is None:
                return left is right
            # 判断节点是否相等
            if left.val != right.val:
                return False
            if not (is_sample_tree(left.left, right.right) and is_sample_tree(left.right, right.left)):
                return False
            return True

        return is_sample_tree(root.left, root.right)
