# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.minPq = []
        self.dfs(root)
        popped = None
        for i in range(k):
            popped = heapq.heappop(self.minPq)
        if popped is None:
            return 0
        return popped
    

    def dfs(self, root):
            if not root:
                return
            heapq.heappush(self.minPq, root.val)
            self.dfs(root.left)
            self.dfs(root.right)


