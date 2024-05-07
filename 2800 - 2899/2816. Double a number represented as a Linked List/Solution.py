class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            res = ListNode()
            temp = head
            while temp:
                next = temp.next
                temp.next = res.next
                res.next = temp
                temp = next
            return res.next

        head = reverse(head)
        res = temp = ListNode()
        mul, carry = 2, 0
        while head:
            x = head.val * mul + carry
            carry = x // 10
            temp.next = ListNode(x % 10)
            temp = temp.next
            head = head.next
        if carry:
            temp.next = ListNode(carry)
        return reverse(res.next)
