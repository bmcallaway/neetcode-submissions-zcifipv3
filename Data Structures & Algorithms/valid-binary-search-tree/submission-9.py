# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        valid = True
        def inorder(root):
            nonlocal prev, valid
            if not root:
                return

            inorder(root.left)
            print("prev:",prev, " root:",root.val)
            if prev is not None and prev >= root.val:
                valid = False
            prev = root.val
            inorder(root.right)
        inorder(root)
        return valid
        