# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        elif root.val < p.val and root.val < q.val:
            root = root.right
            return self.lowestCommonAncestor(root, p, q)
        elif root.val > p.val and root.val > q.val:
            root = root.left
            return self.lowestCommonAncestor(root, p, q)
        elif (p.val < root.val and q.val > root.val) or (q.val < root.val and p.val > root.val):
            return root
        elif (root.val == p.val or root.val == q.val):
            return root

        