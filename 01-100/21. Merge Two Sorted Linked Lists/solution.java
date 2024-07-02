class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode d=new ListNode(0,null);
        ListNode tail=d;
        while(list1!=null || list2!=null)
        {
            if(list1==null)
            {
                tail.next=list2;
                break;
            }
            if(list2==null)
            {
                tail.next=list1;
                break;
            }

            if(list1.val>list2.val)
            {
                tail.next=list2;
                list2=list2.next;
            }
            else
            {
                tail.next=list1;
                list1=list1.next;
            }
            tail=tail.next;
        }
        return d.next;
    }
}
