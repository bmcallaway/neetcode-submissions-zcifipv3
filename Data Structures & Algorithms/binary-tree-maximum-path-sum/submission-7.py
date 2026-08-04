# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#           8
#          / \
#         9   -6
#        / \  / \
#       N. N  5. 9
#
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def getMaxLength(root):
            if not root:
                return 0
            left = max(0, getMaxLength(root.left))
            right = max(0, getMaxLength(root.right))
            return max(0, root.val + max(left, right))

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            res = max(res, root.val + getMaxLength(root.left) + getMaxLength(root.right))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        print(getMaxLength(root.right))
        return res