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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode cur = head;
        int length = 0;
        while(cur != null){
            length++;
            cur = cur.next;
        }
        if(n == length){
            return head.next;
        }
        int index = length - n;
        cur = head;
        for(int i = 0; i < index-1; i++){
            cur = cur.next;
        }
        cur.next = cur.next.next;
        return head;
    }
}
