# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        nodeList = []

        iter = head

        while iter:
            nodeList.append(iter)
            iter = iter.next
        
        removeIdx = len(nodeList) - n

        if removeIdx == 0:
            return head.next
        
        node = nodeList[removeIdx-1]
        node.next = node.next.next

        return head


        
