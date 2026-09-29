# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        inorderIndices = {}

        for i, val in enumerate(inorder):
            inorderIndices[val] = i

        preorderIdx = 0
        def buildBST(l, r):
            nonlocal preorderIdx
            if preorderIdx >= len(preorder) or l > r :
                return None
            val = preorder[preorderIdx]
            preorderIdx += 1
            node = TreeNode(val)
            mid = inorderIndices[val]
            node.left = buildBST(l, mid-1)
            node.right = buildBST(mid+1, r)
            return node
            
        return buildBST(0, len(inorder) - 1)


  #                 5
  #             3.      6
  #          1    4        7
    #         2
  #
  #

