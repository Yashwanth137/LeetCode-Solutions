class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n=len(gas)
        for i in range(0,n):
            tank=gas[i]
            for j in range(i+1,n+i+1):
                if tank<cost[(j-1)%n]:
                    tank=tank-cost[(j-1)%n]
                    break
                tank=tank-cost[(j-1)%n]+gas[(j)%n]
            if tank>=0:
                return i
        return -1
