class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head==null || head.next==null)
        {
            return head;
        }
        ListNode dummy=new ListNode(0);
        dummy.next=head;
        ListNode current=dummy;
        while(current.next!=null && current.next.next!=null)
        {
            ListNode temp1=current.next.next.next;
            ListNode temp2=current.next;
            current.next=current.next.next;
            temp2.next=temp1;
            current.next.next=temp2;
            current=current.next.next;
        }
        return dummy.next; 
    }
}
