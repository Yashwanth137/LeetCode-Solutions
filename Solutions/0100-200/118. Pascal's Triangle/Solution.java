import math as m
class Solution(object):
    @classmethod
    def nCr(cls,i,j):
        return int(m.factorial(i)/(m.factorial(i-j)*m.factorial(j)))
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l=[[] for i in range(numRows)]
    
        for i in range(numRows):
            for j in range(i+ 1):
                if j==0 and j==i:
                    l[i].append(1)
                else:
                    l[i].append(self.nCr(i,j))
        return l
