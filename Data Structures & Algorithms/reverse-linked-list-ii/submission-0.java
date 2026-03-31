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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode iter = head;
        if(left == 1){
            return reverseListTo(head, right-left);
        }
        for(int i = 0; i < left-2; i++){
            iter = iter.next;
        }
        iter.next = reverseListTo(iter.next, right-left);
        return head;
    }
    public ListNode reverseListTo(ListNode head, int length){
        ListNode prev = head;
        for(int i = 0; i <= length; i++){
            prev = prev.next;
        }
        for(int i = 0; i <= length; i++){
            ListNode temp = head.next;
            head.next = prev;
            prev = head;
            head = temp;
        }
        return prev;
    }
}