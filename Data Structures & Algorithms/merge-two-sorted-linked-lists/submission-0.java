/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode();
        ListNode iter = head;
        while(list1 != null || list2 != null){
            System.out.println("No if");
            //if list1 is empty add contents of list2 to current sorted list
            //if list2 is empty add contents of list1 to current sorted list
            //if niether are empty compare and add lower node and move node to next position for that list.
            if(list1 != null && list2 != null){
                System.out.println("If1");
                if(list1.val <= list2.val){
                    iter.next = list1;
                    list1 = list1.next;
                }else{
                    iter.next = list2;
                    list2 = list2.next;
                }

            }else if(list1 != null && list2 == null){
                System.out.println("If2");                
                iter.next = list1;
                list1 = list1.next;
            }else if(list2 != null && list1 == null){
                System.out.println("If3");
                iter.next = list2;
                list2 = list2.next;
            }
            iter = iter.next;
        }
        return head.next;

    }
}