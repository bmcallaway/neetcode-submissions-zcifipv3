# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        
        dummy = head
        removeIdx = length - n

        if removeIdx == 0:
            head = head.next
            return head
        
        for i in range(removeIdx-1):
            dummy = dummy.next
        
        dummy.next = dummy.next.next

        return head


        