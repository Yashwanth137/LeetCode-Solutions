class Solution {
    public ListNode removeNodes(ListNode head) {
        ListNode current=head;
        ListNode prev=null;
        ListNode next=null;
        while(current!=null)
        {
            next=current.next;
            current.next=prev;
            prev=current;
            current=next;
        }
        head=prev;

        ListNode x=head;
        while(x.next!=null)
        {
            if(x.val>x.next.val)
            {
                x.next=x.next.next;
                continue;
            }
            else
                x=x.next;
        }

        current=head;
        next=null;
        prev=null;
        while(current!=null)
        {
            next=current.next;
            current.next=prev;
            prev=current;
            current=next;
        }
        return prev;
    }
}
