class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, curr = 0, 0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                res = max(res, curr)
                curr = 0
        res = max(res, curr)
        return res
