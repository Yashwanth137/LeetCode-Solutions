class Solution {
    public ListNode doubleIt(ListNode head) {
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
        int carry=0;
        int value=0;
        while(x.next!=null)
        {
            value=x.val*2;
            x.val=value%10+carry;
            carry=value/10;

            x=x.next;
        }
        
        value=x.val*2;
        x.val=value%10+carry;
        carry=value/10;
        if(carry==1)
        {
            ListNode newNode=new ListNode(1);
            x.next=newNode;
        }

        current=head;
        prev=null;
        next=null;
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
