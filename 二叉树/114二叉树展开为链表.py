# -*- coding: utf-8 -*-
# @File    : 114二叉树展开为链表.py
# @Des     :


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        nodes = []

        def pre_order(root):
            if not root:
                return

            nodes.append(root)

            pre_order(root.left)
            pre_order(root.right)

        pre_order(root)

        for i in range(1, len(nodes)):
            pre = nodes[i - 1]
            cur = nodes[i]
            pre.left = None
            pre.right = cur

# 不返回任何值,在原链表上修改
