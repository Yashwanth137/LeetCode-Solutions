class Solution {
    public int[] nextLargerNodes(ListNode head) {
        int n=0;
        ListNode current = head;
        ListNode prev=null;
        while(current!=null)
        {
            ListNode next=current.next;
            current.next=prev;
            prev=current;
            current=next;
            n+=1;
        }

        int[] a = new int[n];
        int[] s=new int[n];
        int top=-1;

        current=prev;
        for(int i=n-1;current!=null;i--)
        {
            while(top!=-1 && s[top]<=current.val)
            {
                top-=1;
            }

            if(top==-1)
            {
                a[i]=0;
            }
            else
            {
                a[i]=s[top];
            }
            s[++top]=current.val;
            current=current.next;
        }
        return a;
    }
}
