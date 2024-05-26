# -*- coding: utf-8 -*-
# @File    : 94中序遍历.py
# @Des     :
from idlelib.tree import TreeNode
from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 解法1 dps
class Solution:

    def __init__(self):
        self.res = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return self.res
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)

        return self.res

if __name__ == '__main__':

    pass