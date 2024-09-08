# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next
        
        parts = n // k
        extra = n % k
        
        res = []
        curr = head
        
        for i in range(k):
            part_head = curr
            current_part_size = parts + (1 if extra > 0 else 0)
            extra -= 1
            
            for j in range(current_part_size - 1):
                if curr:
                    curr = curr.next
            
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
            
            res.append(part_head)
        return res
