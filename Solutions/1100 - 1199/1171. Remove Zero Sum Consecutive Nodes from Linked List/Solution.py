class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp=head
        li=[]
        while temp!=None:
            li.append(temp.val)
            temp=temp.next
        sum1=0
        i=0
        while i!=len(li):
            sum1+=li[i]
            for j in range(i+1,len(li)+1):
                if sum1==0:
                    j=j-1
                    del li[i:j+1]
                    i=i-1
                    break
                else:
                    if j==len(li):
                        break
                    sum1+=li[j]
            sum1=0
            i=i+1
            
        temp=ListNode(0)
        x=temp
        for i in li:
            temp.next=ListNode(i)
            temp=temp.next
        return x.next
        
