# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        preorderList = []

        def preorder(root):
            nonlocal preorderList
            if not root:
                return
            preorder(root.left)
            preorderList.append(root.val)
            preorder(root.right)
        
        preorder(root)

        return preorderList[k-1]