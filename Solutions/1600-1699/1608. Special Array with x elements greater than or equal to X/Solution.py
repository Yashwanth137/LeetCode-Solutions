class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(1, len(nums) + 1):
            count = sum(num >= x for num in nums)
            if count == x:
                return x
        return -1
