class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        
        if(head==null || head.next==null)
            return head;
        
        if(left==right)
            return head;
        
        
        ListNode current=head;
        ListNode prev=null;
        for(int i=1;i<left;i++)
        {
            prev=current;
            current=current.next;
        }
        
        ListNode x1=prev;
        ListNode x2=null;
        ListNode r1=current;
        ListNode r2=current;;
        for(int i=left;i<=right;i++)
        {
            r2=current;
            current=current.next;
        }
        x2=current;
        r2.next=null;
        
        ListNode next=null;
        current=r1;
        prev=null;
        while(current!=null)
        {
            next=current.next;
            current.next=prev;
            prev=current;
            current=next;
        }
        if(x1!=null)
            x1.next=r2;
        else
            head=r2;
        r1.next=x2;
        
        return head;
    }
}
