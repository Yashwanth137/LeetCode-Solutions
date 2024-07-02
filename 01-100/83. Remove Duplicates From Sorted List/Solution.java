class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy=new ListNode(0);
        dummy.next=head;
        ListNode current=head;
        while(current!=null && current.next!=null)
        {
            ListNode next=current.next;
            if(current.val<next.val)
                current=current.next;
            else
                current.next=next.next; 
        }
        return dummy.next;
    }
}
