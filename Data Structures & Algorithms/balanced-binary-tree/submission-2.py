# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        leftLength =self.getLength(root.left)
        rightLength = self.getLength(root.right)

        if abs(rightLength - leftLength) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getLength(self, root):
        if root is None:
            return 0
        length = 1 + max(self.getLength(root.left), self.getLength(root.right))
        return length

        # 1
        #2 2
    #.  3   3
    #. 4  4
        
        