class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        ArrayList<Integer> a=new ArrayList<Integer>();
        ListNode cur=head;
        while(cur!=null)
        {
            a.add(cur.val);
            cur=cur.next;
        }
        cur=head;
        for(int i=0;i<a.size();i++)
        {
            if(i==k-1)
                cur.val=a.get(a.size()-k);
            if(i==a.size()-k)
            {
                cur.val=a.get(k-1);
            }
            cur=cur.next;
        }
        
        return head;
    }
}
