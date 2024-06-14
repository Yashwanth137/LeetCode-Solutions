class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                cnt += nums[i-1] + 1 - nums[i]
                nums[i] = nums[i-1] + 1
        return cnt
