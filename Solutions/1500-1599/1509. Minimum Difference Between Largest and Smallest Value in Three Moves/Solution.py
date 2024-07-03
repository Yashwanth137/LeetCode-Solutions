class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 3
        
        if len(nums) <= 4:
            return 0
        
        nums.sort()

        diff = float('inf')
        
        while i <= 3 and j >= 0:
            diff = min(diff,nums[n - 1 - j] - nums[i])
            i += 1
            j -= 1

        return diff 
