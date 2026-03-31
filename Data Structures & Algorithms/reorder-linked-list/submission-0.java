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
    public void reorderList(ListNode head) {
        List<ListNode> list = new ArrayList<>();
        while(head != null){
            list.add(head);
            head = head.next;
        }
        int l = 0;
        int r = list.size() - 1;
        while(l < r){
            list.get(l).next = list.get(r);
            l++;
            if(l >= r){
                break;
            }
            list.get(r).next = list.get(l);
            r--;
        }
        list.get(l).next = null;
    }

}
