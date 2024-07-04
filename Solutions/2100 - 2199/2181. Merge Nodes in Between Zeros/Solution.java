class Solution {
    public ListNode mergeNodes(ListNode head) {
        ListNode prev=head;
        ListNode current=head.next;
        while(current!=null)
        {
            if(current.val==0)
            {
                prev.next=current;
                if(current.next==null)
                    prev.next=null;
                else
                    prev=current;
            }
            else
            {
                prev.val+=current.val;
            }
            current=current.next;
        }
        return head;
    }
}
