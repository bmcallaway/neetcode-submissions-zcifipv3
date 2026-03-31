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
        List<ListNode> nodes = new ArrayList<>();
        while(cur != null){
            nodes.add(cur);
            cur = cur.next;
        }
        if(n == nodes.size()){
            return head.next;
        }
        int index = nodes.size() - n;
        System.out.println("Index: " + index);
        System.out.println("Nodes.get(n-1): " + nodes.get(n-1).val);
        nodes.get(index-1).next = nodes.get(index).next;
        return nodes.get(0);
    }
}
