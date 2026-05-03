# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        nodes = []

        cur = head

        while cur:
            nodes.append(cur)
            cur = cur.next

        l = 0
        r = len(nodes)-1

        reorderedList = []
        while l < r:
            reorderedList.append(nodes[l])
            reorderedList.append(nodes[r])
            l += 1
            r -= 1
            if l == r:
                reorderedList.append(nodes[l])
                break;

        cur = head

        for i in range(1, len(reorderedList)):
            cur.next = reorderedList[i]
            cur = cur.next

        cur.next = None
        
        