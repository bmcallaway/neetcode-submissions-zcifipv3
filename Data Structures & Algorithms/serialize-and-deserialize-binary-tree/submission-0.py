# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(root):
            nonlocal res
            if not root:
                res.append("n")
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)

        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = iter(data.split(','))
        
        def preorder():
            val = next(values)
            if val == "n":
                return
            node = TreeNode(int(val))
            node.left = preorder()
            node.right = preorder()
            return node

        return preorder()
            
            



