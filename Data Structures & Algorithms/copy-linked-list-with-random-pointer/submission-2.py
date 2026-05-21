"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nodes = {}
        dummy = head
        while dummy:
            node = Node(dummy.val)
            nodes[dummy] = node
            dummy = dummy.next

        dummy = head
        while dummy:
            node = nodes[dummy]
            node.next = nodes.get(dummy.next)
            node.random = nodes.get(dummy.random)
            dummy = dummy.next

        return nodes[head]
        