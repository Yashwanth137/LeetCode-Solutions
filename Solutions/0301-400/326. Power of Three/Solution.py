class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        res = math.log(n, 3)
        return abs(res - round(res)) < 1e-10
