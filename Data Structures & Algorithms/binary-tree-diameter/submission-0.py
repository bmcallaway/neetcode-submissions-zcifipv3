# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxDiameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.dfs(root)
        return self.maxDiameter
    def dfs(self, root):
        if root is None:
            return
        left = self.getLength(root.left)
        right = self.getLength(root.right)
        diameter = left + right
        self.maxDiameter = max(self.maxDiameter, diameter)
        self.dfs(root.left)
        self.dfs(root.right)
        
    def getLength(self, root):
        if root is None:
            return 0
        length = 1 + max(self.getLength(root.left), self.getLength(root.right))
        return length