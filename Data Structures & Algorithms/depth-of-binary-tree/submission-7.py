# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        #   2 3
        #   
        #  
        #   


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = deque()
        stack.append(root)
        depth = 0;
        def bfs(root):
            nonlocal stack, depth
            while stack:
                length = len(stack)
                while length > 0:
                    node = stack.popleft()
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                    length -= 1
                depth += 1
                layer = []
        bfs(root)
        return depth
                



        