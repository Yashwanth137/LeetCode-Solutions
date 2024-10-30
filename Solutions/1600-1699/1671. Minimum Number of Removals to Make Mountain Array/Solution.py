class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    left[i] = max(left[i], left[j] + 1)
        
        right = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    right[i] = max(right[i], right[j] + 1)
        
        min_removals = float('inf')
        for i in range(1, n - 1):
            if left[i] > 1 and right[i] > 1:  
                min_removals = min(min_removals, n - (left[i] + right[i] - 1))
        
        return min_removals
