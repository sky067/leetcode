# -*- coding: utf-8 -*-
# @File    : 104二叉树的最大深度.py
# @Des     :
from idlelib.tree import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#dps
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)


if __name__ == '__main__':
    s = Solution()
    # root = TreeNode()
