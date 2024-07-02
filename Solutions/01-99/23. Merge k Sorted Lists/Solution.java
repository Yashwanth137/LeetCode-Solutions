class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode head=new ListNode(0);
        ListNode current=head;
        if(lists.length==0)
        {
            return null;
        }
        ListNode list1=lists[0];
        if(lists.length==1)
        {
            return lists[0];
        }
        for(int i=1;i<lists.length;i++)
        {
            ListNode list2=lists[i];
            while(list1!=null && list2!=null)
            {
                if(list1.val<list2.val)
                {
                    current.next=list1;
                    list1=list1.next;
                }
                else
                {
                    current.next=list2;
                    list2=list2.next;
                }
                current=current.next;
            }
            while(list1!=null)
            {
                current.next=list1;
                list1=list1.next;
                current=current.next;
            }
            while(list2!=null)
            {
                current.next=list2;
                list2=list2.next;
                current=current.next;
            }
            list1=head.next;
            current=head;
        }
        return head.next;
    }
}
