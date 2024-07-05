# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def critical(prev, curr, nxt):
            return (prev.val > curr.val < nxt.val or prev.val < curr.val > nxt.val)
        
        prev, curr = head, head.next
        nxt = curr.next
        min_res, max_res = float("inf"), -1

        ind1, ind2, i = 0, 0, 1
        while nxt:
            if critical(prev, curr, nxt):
                if ind1:
                    max_res = i - ind1
                    min_res = min(min_res, i - ind2)
                else:
                    ind1 = i
                ind2 = i
            prev, curr, nxt = curr, nxt, nxt.next
            i += 1
            
        if min_res == float("inf"):
            min_res = -1

        return [min_res, max_res]
