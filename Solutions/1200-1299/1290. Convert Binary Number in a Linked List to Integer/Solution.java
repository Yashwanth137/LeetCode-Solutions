class Solution {
    public int getDecimalValue(ListNode head) {
        int n=0;
        ListNode current=head;
        while(current!=null)
        {
            n+=1;
            current=current.next;
        }
    
        int sum=0;
        current=head;
        for(int i=n-1;i>=0;i--)
        {
            sum+=current.val*Math.pow(2,i);
            current=current.next;
        }

        return sum;
    }
}
