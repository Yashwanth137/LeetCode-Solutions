class Solution {
    public ListNode deleteMiddle(ListNode head) {
        int n=-1;
        ListNode x=head;
        while(x!=null)
        {
            x=x.next;
            n=n+1;
        }
        int middle=(n+1)/2;
        n=-1;
        ListNode cur=new ListNode(0);
        cur.next=head;
        x=cur;
        for(int i=0;i<middle;i++)
        {
            x=x.next;
        }
        x.next=x.next.next;
        return cur.next;
    }
}
