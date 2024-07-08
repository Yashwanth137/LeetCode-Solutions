class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = [i for i in range(1,n+1)]
        i, pos = 0,0
        while len(res) > 1:
            pos = (i + k -1)%len(res)
            del res[pos]
            i = pos

        return res[0]
