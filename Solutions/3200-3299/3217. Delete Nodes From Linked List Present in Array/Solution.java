class Solution {
    public ListNode modifiedList(int[] nums, ListNode head) {
        HashMap<Integer,Boolean> map = new HashMap<>();
        for(int num: nums)
        {
            map.put(num,true);
        }
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode prev=dummy;
        ListNode cur=head;
        
        while(cur!=null)
        {
            if(map.containsKey(cur.val))
            {
                prev.next=cur.next;
                cur=prev.next;
            }
            else
            {
                prev=cur;
                cur=cur.next;
            }
        }
        
        return dummy.next;
    }
}
