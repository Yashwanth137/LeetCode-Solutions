class Solution(object):
    def getRow(self, rowIndex):
        l=[]
        for j in range(rowIndex+1):
            l.append(int(math.factorial(rowIndex)/(math.factorial(rowIndex-j)*math.factorial(j))));
        return l
