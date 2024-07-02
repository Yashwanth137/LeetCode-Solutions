class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode current=l1;
        ListNode next=null;
        ListNode prev=null;
        
        while(current!=null)
        {
            next=current.next;
            current.next=prev;
            prev=current;
            current=next;
        }
        l1=prev;
        
        next=null;
        prev=null;
        current=l2;
        
        while(current!=null)
        {
            next=current.next;
            current.next=prev;
            prev=current;
            current=next;
        }
        l2=prev;
        
        ListNode newNode=new ListNode(-1);
        
        int carry=0;
        while(l2!=null||l1!=null||carry!=0)
        {
            int sum=carry;
            if(l1!=null&&l2!=null)
            {
                sum+=l2.val+l1.val;
                l2=l2.next;
                l1=l1.next;
            }
            else if(l1==null&&l2!=null)
            {
                sum+=l2.val;
                l2=l2.next;
            }
            else if(l2==null&&l1!=null)
            {
                sum+=l1.val;
                l1=l1.next;
            }
            ListNode x=new ListNode(sum%10,newNode);
            newNode=x;
            carry=sum/10;
        }
        
        current=newNode;
        prev=null;
        while(current.next!=null)
        {
            prev=current;
            current=current.next;
        }
        prev.next=null;
        return newNode;
    }
}
