class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, res = len(nums), 0

        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                res += 1
        
        return res if all(num == 1 for num in nums) else -1
