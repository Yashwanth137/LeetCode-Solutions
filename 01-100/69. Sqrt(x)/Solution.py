class Solution:
    def mySqrt(self, x: int) -> int:
        i, res = 1,0
        while x > 0:
            x -= i
            i += 2
            res += 1
        if(x < 0):
            res -= 1
        return res
