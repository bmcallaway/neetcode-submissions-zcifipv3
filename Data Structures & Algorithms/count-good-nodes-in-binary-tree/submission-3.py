# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
            #  2
            #/   \
        #   N     4
        #        / \
        #       10  8
        #          /
        #         4
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(root, maxVal):
            if not root:
                return 0
            print(root.val, maxVal)
            if root.val >= maxVal:
                maxVal = root.val
                return 1 + dfs(root.left, maxVal) + dfs(root.right, maxVal)
            else:
                return dfs(root.left, maxVal) + dfs(root.right, maxVal)

        #print(dfs(root))
        return dfs(root, float("-inf"))

    
            
            