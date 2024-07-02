class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode lx=new ListNode(0);
        ListNode gx=new ListNode(0);
        
        ListNode l1=lx;
        ListNode l2=gx;
        ListNode current=head;
        while(current!=null)
        {
            if(current.val<x)
            {
                lx.next=current;
                lx=lx.next;
            }
            else
            {
                gx.next=current;
                gx=gx.next;
            }
            current=current.next;
        }
        lx.next=null;
        gx.next=null;
        if(l1.next==null)
            l1.next=l2.next;
        else
            lx.next=l2.next;
        return l1.next;
    }
}
