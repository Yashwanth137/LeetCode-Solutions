class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            n = nums.index(val)
            del nums[n]
        return len(nums)
