class Solution(object):
    def sortList(self, head):
        li=[]
        cur = head
        while cur!=None:
            li.append(cur.val)
            cur = cur.next
        
        li.sort()
        cur = head 
        for val in li:
            cur.val=val
            cur = cur.next
        
        return head
