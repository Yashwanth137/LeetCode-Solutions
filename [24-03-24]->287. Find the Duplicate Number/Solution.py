class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def is_duplicate(no: int) -> bool:
            count = sum(1 for num in nums if num <= no)
            return count > no

        left, right = 1, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if is_duplicate(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
