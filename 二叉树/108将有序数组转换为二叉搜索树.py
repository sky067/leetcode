# -*- coding: utf-8 -*-
# @File    : 108将有序数组转换为二叉搜索树.py
# @Des     :


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        1. 升序列表中间数字为根节点
        2. 列表以中间分割，左边为左子树的根，右边为右子树的根
        3. 递归的进行 1,2
        4. 注意递归结束条件
        """

        def dfs(nums, left, right):
            if left > right:
                return
            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = dfs(nums, left, mid - 1)
            root.right = dfs(nums, mid + 1, right)
            return root

        return dfs(nums, 0, len(nums) - 1)
