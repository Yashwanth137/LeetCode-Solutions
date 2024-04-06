class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            while nums[idx] != nums[nums[idx] - 1]:
                nums[nums[idx] - 1], nums[idx] = nums[idx], nums[nums[idx] - 1]
        return [val for idx, val in enumerate(nums) if val != idx + 1]
