class Solution:
    def findComplement(self, num: int) -> int:
        res, index = 0, 0
        while num > 0:
            if num % 2 == 0:  
                res += 2 ** index
            index += 1
            num //= 2
        return res
