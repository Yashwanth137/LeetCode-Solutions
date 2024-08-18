class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [0]*n
        nums[0] = 1
        i2 = i3 = i5 = 0
        mul_2, mul_3, mul_5 = 2, 3, 5

        for i in range(1, n):
            nex_t = min(mul_2, mul_3, mul_5)
            nums[i] = nex_t

            if nex_t == mul_2:
                i2 += 1
                mul_2 = nums[i2]*2

            if nex_t == mul_3:
                i3 += 1
                mul_3 = nums[i3]*3

            if nex_t == mul_5:
                i5 += 1
                mul_5 = nums[i5]*5

        return nums[n-1]
