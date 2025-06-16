class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        minn = nums[0]
        for i in range(1, len(nums)):
            if minn < nums[i]:
                res = max(res, nums[i] - minn)
            else:
                minn = nums[i]
                
        return res
