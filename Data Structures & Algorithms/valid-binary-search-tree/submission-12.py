# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#               0
#              / \
#            -1k  1k
#                 /
#                0
#
#
#
#
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorderList = []

        def inorder(root):
            nonlocal inorderList
            if not root:
                return None
            inorder(root.left)
            inorderList.append(root.val)
            inorder(root.right)

        inorder(root)
        prevVal = float("-inf")
        for node in inorderList:
            if node <= prevVal:
                return False
            prevVal = node

        return True