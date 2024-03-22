class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current, fast_ptr = head, head.next
        while fast_ptr and fast_ptr.next:
            current, fast_ptr = current.next, fast_ptr.next.next
        prev, current = None, current.next
        while current:
            temp = current.next
            current.next = prev
            prev, current = current, temp
        while prev:
            if prev.val != head.val:
                return False
            prev, head = prev.next, head.next
        return True
