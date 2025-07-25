class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode middle = head;
        ListNode end = head;

        // jump end by two nodes and middle by one
        while (end != null && end.next != null) {
            middle = middle.next;
            end = end.next.next;
        }

        return middle;
    }
}