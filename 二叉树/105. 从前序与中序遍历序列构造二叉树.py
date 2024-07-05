# -*- coding: utf-8 -*-
# @File    : 105. 从前序与中序遍历序列构造二叉树.py
# @Des     :


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        前序找根，中序找左右子树

        return: TreeNode()
        """

        if not preorder:
            return None

        # 前序中取根节点
        root_val = preorder[0]

        # 中序遍历找到根节点的左右子树长度
        root_ind = inorder.index(root_val)  # 根节点在中序的位置
        #left_len = len(inorder[ : root_ind])  # 左子树长度
        left_len=root_ind

        # 根据在中序的长度在前序中找到左右子树
        left_preorder = preorder[1 : left_len+1]
        left_inorder = inorder[ : left_len]

        right_preorder = preorder[left_len + 1 : ]
        right_inorder = inorder[left_len + 1 : ]

        root = TreeNode(root_val)
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

"""
思路:
1. 在前序遍历中获取根节点
2. 根据根节点在中序遍历中获取左右子树的长度
3. 在前序遍历中根据左右子树长度获取左右子树
4. 递归的进行 1,2,3

"""