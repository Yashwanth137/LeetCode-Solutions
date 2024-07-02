public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head==null||head.next==null)
            return null;
        ListNode slow=head;
        ListNode fast=head.next;
        
        while(fast!=null&&fast.next!=null)
        {
            if(slow==fast)
                break;
            slow=slow.next;
            fast=fast.next.next;
        }
        
        if(slow==fast)
        {
            slow=head;
            while(slow!=fast.next)
            {
                slow=slow.next;
                fast=fast.next;
            }
            return fast.next;
        }
        else
            return null;
    }
}
