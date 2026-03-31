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
    public boolean hasCycle(ListNode head) {
        if(head == null){
            return false;
        }
        Set<ListNode> seen = new HashSet();
        while(head.next != null){
            seen.add(head);
            if(seen.contains(head.next)){
                return true;
            }
            head = head.next;
        }
        return false;
    }
}
