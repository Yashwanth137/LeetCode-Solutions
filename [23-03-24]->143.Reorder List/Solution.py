class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast_ptr = slow_ptr = head
        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        current = slow_ptr.next
        slow_ptr.next = None

        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous, current = current, temp
        current = head

        while previous:
            temp = previous.next
            previous.next = current.next
            current.next = previous
            current, previous = previous.next, temp
