class Solution {
    public boolean isPalindrome(ListNode head) {
        Stack<Integer> stack=new Stack<Integer>();
        ListNode current=head;
        while(current!=null)
        {
            stack.push(current.val);
            current=current.next;
        }
        
        boolean ispal=true;
        current=head;
        while(current!=null)
        {
            if(current.val==stack.pop())
                ispal=true;
            else
                return false;
            current=current.next;
        }
        return true;
    }
}
