class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null || head.next==null)
            return head;
        ListNode current=head;
        int count=0;
        while(current!=null)
        {
            count+=1;
            current=current.next;
        }
        k=k%count;
        while(k!=0)
        {
            ListNode x=head;
            while(x.next.next!=null)
            {
                x=x.next;
            }
            ListNode y=x.next;
            y.next=head;
            x.next=null;
            head=y;
            k=k-1;
        }

        return head;
    }
}
