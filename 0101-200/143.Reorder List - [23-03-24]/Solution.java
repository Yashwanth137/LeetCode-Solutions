class Solution {
    public void reorderList(ListNode head) {
        
        if(head==null || head.next==null)
            return;
        
        ListNode fast=head;
        ListNode slow=head;
        while(fast!=null && fast.next!=null)
        {
            slow=slow.next;
            fast=fast.next.next;
        }

        ListNode current=slow.next;
        slow.next=null;

        ListNode prev=null;
        ListNode next=null;
        while(current!=null)
        {
            next=current.next;
            current.next=prev;
            prev=current;
            current=next;
        }

        ListNode first=head;
        ListNode second=prev;

        while(second!=null)
        {
            ListNode firstNext=first.next;
            ListNode secondNext=second.next;

            first.next=second;
            second.next=firstNext;
            first=firstNext;
            second=secondNext;
        }
    }
}
