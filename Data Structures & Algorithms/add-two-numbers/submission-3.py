# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        
        carry = False
        while l1 or l2:
            digSum = l1.val if l1 else 0
            digSum += l2.val if l2 else 0
            if carry:
                digSum += 1
            if digSum > 9:
                secDig = int(str(digSum)[1])
                newNode = ListNode(secDig)
                carry = True
            else:
                newNode = ListNode(digSum)
                carry = False
            dummy.next = newNode
            dummy = dummy.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        if carry:
            newNode = ListNode(1)
            dummy.next = newNode
            dummy = dummy.next

        return head.next