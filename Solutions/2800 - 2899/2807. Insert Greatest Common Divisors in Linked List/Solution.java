class Solution {
    public static int gcd(int a,int b)
    {
        while(b!=0)
        {
            int temp=b;
            b=a%b;
            a=temp;
        }
        return a;
    }
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        if(head==null || head.next==null)
            return head;
        
        ListNode cur = head.next;
        ListNode prev = head;
        
        while(cur!=null)
        {
            int val=gcd(prev.val,cur.val);
            ListNode newNode = new ListNode(val,cur);
            prev.next=newNode;
            prev=cur;
            cur=cur.next;
        }
        return head;
    }
}
