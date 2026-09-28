# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, currMax):
            nonlocal res
            if not root:
                return
            if root.val >= currMax:
                currMax = root.val
                res += 1
            dfs(root.left, currMax)
            dfs(root.right, currMax)
        
        dfs(root, root.val)
        return res

