"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapped = {}

        def dfs(node):
            if not node or node in mapped:
                return
            newNode = Node(node.val)
            mapped[node] = newNode
            for neighbor in node.neighbors:
                dfs(neighbor)
                newNode.neighbors.append(mapped.get(neighbor))

        dfs(node)

        return mapped.get(node)