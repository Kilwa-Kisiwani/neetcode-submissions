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
    public ListNode reverseList(ListNode head) {
        Stack<ListNode> q = new Stack<ListNode>();
        while (head != null) {
            q.push(head);
            ListNode next = head.next;
            head.next = null;
            head = next;
        }
        ListNode newHead = null;
        ListNode curr = null;
        while(!q.isEmpty()) {
            if (newHead == null) {
                newHead = q.pop();
                curr = newHead;
            } else {
                curr.next = q.pop();
                curr = curr.next;
            }
        }
        return newHead;
    }
}
