class Solution {
    public static ListNode reverse(ListNode head)
    {
        ListNode prev=null;
        ListNode current=head;
        ListNode next=null;

        while(current!=null)
        {
            next=current.next;
            current.next=prev;
            prev=current;
            current=next;
        }
        return prev;
    }
    public ListNode reverseKGroup(ListNode head, int k) {
        if(head==null || head.next==null || k==1)
        {
            return head;
        }

        ListNode current=head;
        ListNode start=head;
        ListNode last=head;

        ListNode prev=null;
        for(int i=1; current!=null; i++)
        {
            if(i==k)
            {
                last=current;
                current=current.next;
                last.next=null;
                head=reverse(start);
                prev=start;
                start=current;
            }
            else if(i%k == 0)
            {
                last=current;
                current=current.next;
                last.next=null;
                prev.next=reverse(start);
                prev=start;
                start=current;
            }
            else
            {
                current = current.next;
            }
        }
        if(start!=null)
        {
            prev.next=start;
        }

        return head;
    }
}
