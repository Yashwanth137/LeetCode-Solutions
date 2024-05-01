class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target > max(nums):
            return len(nums)
        elif target < min(nums):
            return 0
        else:
            for i in nums:
                if target < i:
                    return nums.index(i)
