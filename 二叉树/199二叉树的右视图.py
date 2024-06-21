# -*- coding: utf-8 -*-
# @File    : 199二叉树的右视图.py
# @Des     :


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
思路:
先递归右子树，再递归左子树，当某个深度首次到达时，对应的节点就在右视图中。
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(root, depth):
            if not root:
                return
            if depth == len(ans):
                ans.append(root.val)
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)

        dfs(root, 0)
        return ans
