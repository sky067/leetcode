# -*- coding: utf-8 -*-
# @File    : 102二叉树的层次遍历.py
# @Des     :


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = []
        q.append(root)

        temp_q = []
        ans = []
        cur_ans = []
        while q:

            node = q.pop(0)
            cur_ans.append(node.val)
            if node.left:
                temp_q.append(node.left)
            if node.right:
                temp_q.append(node.right)
            if not q:
                q = temp_q
                temp_q = []
                ans.append(cur_ans)
                cur_ans = []
        return ans
