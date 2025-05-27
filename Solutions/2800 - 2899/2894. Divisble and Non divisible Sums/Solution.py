class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums = [i for i in range(1, n+1)]
        n1, n2 = 0, 0
        for i in nums:
            if i % m == 0:
                n1 += i
            else:
                n2 += i

        return n2-n1
