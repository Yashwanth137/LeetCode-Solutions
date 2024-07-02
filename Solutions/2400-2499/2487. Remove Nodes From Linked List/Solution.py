class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        stack = []
        for v in res:
            while stack and stack[-1] < v:
                stack.pop()
            stack.append(v)
        temp = ListNode()
        head = temp
        for v in stack:
            head.next = ListNode(v)
            head = head.next
        return temp.next
