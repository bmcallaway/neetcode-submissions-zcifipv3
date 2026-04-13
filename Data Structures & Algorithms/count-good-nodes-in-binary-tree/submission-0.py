# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#       3
#     3   NULL
#   4   2
#       

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        self.res = 1
        self.dfs(root, root.val)
        return self.res

    def dfs(self, root, currMax):
        if root:
            if root.left:
                if root.left.val >= currMax:
                    self.res += 1
                    self.dfs(root.left, root.left.val)
                else: self.dfs(root.left, currMax)
            if root.right:
                if root.right.val >= currMax:
                    self.res += 1
                    self.dfs(root.right, root.right.val)
                else: self.dfs(root.right, currMax)


                
    

