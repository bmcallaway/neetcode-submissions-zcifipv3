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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        String num1 = "";
        String num2 = "";

        
        while(l1 != null){
            num1 = l1.val + num1;
            l1 = l1.next;
        }

        while(l2 != null){
            num2 = l2.val + num2;
            l2 = l2.next;
        }        
        int val1 = Integer.valueOf(num1);
        int val2 = Integer.valueOf(num2);
        int ans = val1 + val2;

        String ansString = Integer.toString(ans);
        char[] ansArray = ansString.toCharArray();

        ListNode prev = null;
        ListNode newNode;
        for(int i = 0; i < ansArray.length; i++){
            newNode = new ListNode(ansArray[i] - '0', prev);
            prev = newNode;
        }
        return prev;
    }
}
