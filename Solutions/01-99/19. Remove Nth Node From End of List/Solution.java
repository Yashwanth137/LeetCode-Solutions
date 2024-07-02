class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode x=head;
        int length=0;
        while(x!=null)
        {
            length+=1;
            x=x.next;
        }
        n=length-n+1;
        x=head;
        length=0;
        ListNode curr=new ListNode(0);
        curr.next=head;
        x=curr;
        while(x!=null)
        {
            if(++length==n)
                x.next=x.next.next;
            x=x.next;
        }
        return curr.next;
    }
}
