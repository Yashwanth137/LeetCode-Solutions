class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dum=new ListNode(-1,head);
        ListNode x=dum;
        while(x.next!=null)
        {
            if(x.next.val==val)
            {
                x.next=x.next.next;
            }
            else
                x=x.next;
        }
        return dum.next;
    }
}
