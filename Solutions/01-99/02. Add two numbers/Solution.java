class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode sum=new ListNode(0,null);
        ListNode tail=sum;
        int carry=0;
        while(l1!=null || l2!=null || carry!=0)
        {
            int sum1=carry;
            if(l1!=null && l2!=null)
            {
                sum1+=l1.val+l2.val;
                ListNode newNode=new ListNode(sum1%10,null);
                sum.next=newNode;

                l1=l1.next;
                l2=l2.next;
            }
            else if(l1!=null)
            {
                sum1+=l1.val;
                ListNode newNode=new ListNode(sum1%10,null);
                sum.next=newNode;

                l1=l1.next;
            }
            else if(l2!=null)
            {
                sum1+=l2.val;
                ListNode newNode=new ListNode(sum1%10,null);
                sum.next=newNode;

                l2=l2.next;
            }
            else
            {
                ListNode newNode=new ListNode(sum1%10,null);
                sum.next=newNode;
            }
            carry=sum1/10;
            sum=sum.next;
        }
        return tail.next;
    }
}
