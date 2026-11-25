"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def dfs(node):
            if not node or node.val in clones:
                return
            clone = Node(node.val)
            clones[node.val] = clone
            for neighbor in node.neighbors:
                dfs(neighbor)
                clone.neighbors.append(clones.get(neighbor.val))
            
        dfs(node)
        print(clones)
        return clones.get(node.val) if len(clones) > 0 else None