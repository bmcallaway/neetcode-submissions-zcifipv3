# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        values = []

        def preorder(root):
            nonlocal values
            if not root:
                values.append("n")
                return
            values.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ",".join(values)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = iter(data.split(","))
        def preorder(val):
            if val == "n":
                return
            node = TreeNode(val)
            val = next(values)
            print("val:",val)
            node.left = preorder(val)
            node.right = preorder(next(values))
            return node
        return preorder(next(values))





