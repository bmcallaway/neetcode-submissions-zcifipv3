# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        smallest = 0
        def dfs(root):
            nonlocal cnt, smallest
            if not root:
                return
            dfs(root.left)
            cnt += 1
            if cnt == k:
                smallest = root.val
            dfs(root.right)
        dfs(root)
        return smallest