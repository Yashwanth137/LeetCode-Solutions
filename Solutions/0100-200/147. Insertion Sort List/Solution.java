class Solution {
    public ListNode insertionSortList(ListNode head){
        if(head == null || head.next == null)
            return head;
        ListNode dummy = new ListNode(0);
        ListNode toInsert,preInsert;
        dummy.next = head;
        
        ListNode cur = head;
        while(cur != null && cur.next != null)
        {
            if(cur.val<cur.next.val)
            {
                cur=cur.next;
            }
            else
            {
                preInsert = dummy;
                toInsert = cur.next;
                while(preInsert.next.val<toInsert.val)
                {
                    preInsert=preInsert.next;
                }
                cur.next=toInsert.next;
                toInsert.next=preInsert.next;
                preInsert.next=toInsert;
            }   
        }
        return dummy.next;
    }
}
