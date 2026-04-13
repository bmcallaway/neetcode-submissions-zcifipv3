# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, inorderList):
        if root:
            if root.left:
                self.dfs(root.left, inorderList)
            inorderList.append(root.val)
            print(root.val)
            if root.right: self.dfs(root.right,inorderList)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorderList = []
        self.dfs(root, inorderList)
        return inorderList

    
        
