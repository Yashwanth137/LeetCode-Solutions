public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode p1=headA;
        ListNode p2=headB;
        int c1=0;
        int c2=0;
        if(p1==null || p2==null)
            return null;

        while(p1!=null ||p2!=null)
        {
            if(p1!=null)
            {
                p1=p1.next;
                c1+=1;
            }
            if(p2!=null)
            {
                p2=p2.next;
                c2+=1;
            }
        }
        p1=headA;
        p2=headB;
        if(c1>c2)
        {
            while(c1!=c2)
            {
                p1=p1.next;
                c1-=1;
            }
        }
        else
        {
            while(c2!=c1)
            {
                p2=p2.next;
                c2-=1;
            }
        }
        while(p1!=null)
        {
            if(p1==p2)
                return p1;
            p1=p1.next;
            p2=p2.next;
        }
        return null;
    }
}
