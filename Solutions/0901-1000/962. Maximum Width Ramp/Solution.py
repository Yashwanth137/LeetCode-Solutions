class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                res = max(res, j - stack.pop())

        return res
