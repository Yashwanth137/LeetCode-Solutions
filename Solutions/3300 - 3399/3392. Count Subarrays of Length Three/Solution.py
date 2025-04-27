class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 2):
            first = nums[i]
            mid = nums[i + 1]
            last = nums[i + 2]
            if first + last == mid/2:
                res += 1
        return res
