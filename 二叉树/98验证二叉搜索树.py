# -*- coding: utf-8 -*-
# @File    : 98验证二叉搜索树.py
# @Des     :


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre = -inf

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        空树也是二叉搜索树
        """
        # 使用中序遍历，递归判断当前节点 > 上一节点

        if not root:
            return True
        left = self.isValidBST(root.left)

        if root.val > self.pre:
            self.pre = root.val
            # 不断地遍历，直到找到一个不符合要求的
        else:
            return False

        right = self.isValidBST(root.right)
        return left and right








