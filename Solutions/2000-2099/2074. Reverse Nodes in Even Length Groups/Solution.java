class Solution {
    public static ListNode reverse1(ListNode head)
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


    public static ListNode reverse(ListNode head,int k,boolean todo)
    {
        if(head==null || head.next==null )
        {
            return head;
        }

        int c=0;
        ListNode temp=head;
        while(temp!=null && c<k-1)
        {
            temp=temp.next;
            c+=1;
        }


        if(temp==null)
        {
            if(c%2==0)
            {
                return reverse1(head);
            }
            return head;
        }

        ListNode rest=temp.next;
        temp.next=null;
        if(todo)
        {
            head=reverse1(head);
        }
        temp=head;
        while(temp.next!=null)
        {
            temp=temp.next;
        }
        temp.next=reverse(rest,k+1,todo?false:true);
        return head;
    }
    
    public ListNode reverseEvenLengthGroups(ListNode head) {
        return reverse(head,1,false);
    }
}
