class Solution {
    public ListNode middleNode(ListNode head) {
        int length=0;
        ListNode current=head;
        while(current!=null)
        {
            length+=1;
            current=current.next;
        }
        
        int n=(length)/2;
        current=head;
        for(int i=0;i<n;i++)
        {
            current=current.next;
        }
        return current;
    }
}
