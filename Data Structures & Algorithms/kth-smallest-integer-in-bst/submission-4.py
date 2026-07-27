# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted = []
        count = 0
        result = 0
        def inorder(root):
            nonlocal count, result
            if not root:
                return
            inorder(root.left)
            count += 1

            if count == k:
                result = root.val
                
            inorder(root.right)
        inorder(root)
        return result