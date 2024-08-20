class Solution {
    public int pairSum(ListNode head) {
        ListNode prev=null;
        ListNode cur=head;
        ListNode next=head.next;
        
        while(next!=null && next.next!=null)
        {
            cur=cur.next;
            next=next.next.next;
        }
        
        next=cur.next;
        cur.next=null;
        
        cur=next;
        next=null;
        while(cur!=null)
        {
            next=cur.next;
            cur.next=prev;
            prev=cur;
            cur=next;
        }
        
        
        int max=0;
        while(head!=null)
        {
            if((head.val+prev.val)>max)
                max=head.val+prev.val;
            head=head.next;
            prev=prev.next;
        }
        
        return max;
    }
}
