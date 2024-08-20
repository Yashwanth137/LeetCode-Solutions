class Solution {
    public ListNode[] splitListToParts(ListNode head, int k) {
        ListNode current=head;
        int n=0;
        while(current!=null)
        {
            n=n+1;
            current=current.next;
        }

        ListNode[] a=new ListNode[k];
        current=head;

        int i=1,j=0;
        for(j=0;j<n%k;j++)
        {
            a[j]=current;
            for(i=1;i<(n/k)+1;i++)
            {
                if(current!=null)
                {
                    current=current.next;
                }
            }
            if(current!=null)
            {
                head=current.next;
                current.next=null;
                current=head;
            }
        }
        for(;j<k;j++)
        {
            a[j]=current;
            for(i=1;i<n/k;i++)
            {
                if(current!=null)
                {
                    current=current.next;
                }
            }
            if(current!=null)
            {
                head=current.next;
                current.next=null;
                current=head;
            }
        }

        return a;
    }
}
