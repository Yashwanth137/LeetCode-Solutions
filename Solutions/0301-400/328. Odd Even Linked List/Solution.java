class Solution {
    public ListNode oddEvenList(ListNode head) {
        if(head==null || head.next==null)
            return head;
        ListNode odd=new ListNode(0);
        ListNode even=new ListNode(0);
        ListNode current=head;
        
        ListNode odd1=odd;
        ListNode even1=even;
        
        for(int i=1;current!=null;i++)
        {
            if(i%2!=0)
            {
                even.next=current;
                even=even.next;
            }
            else
            {
                odd.next=current;
                odd=odd.next;
            }
            current=current.next;
        }
        odd.next=null;
        even.next=null;
        even.next=odd1.next;
        return even1.next;
    }
}
