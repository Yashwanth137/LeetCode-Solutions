class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n):
            left, right = i + 1, n - 1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] < lower:
                    left = mid + 1
                else:
                    right = mid - 1

            low_bound = left

            left, right = i + 1, n - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] <= upper:
                    left = mid + 1
                else:
                    right = mid - 1

            high_bound = right

            if low_bound <= high_bound:
                count += high_bound - low_bound + 1

        return count
