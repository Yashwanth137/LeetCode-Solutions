class Solution(object):
    def singleNumber(self, nums):
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
            if d[i]==3:
                d.pop(i)

        return d.keys()[0]
