class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0

        current_sum = 0
        max_sum = 0
        window = set()

        left = 0
        for right in range(n):
            while nums[right] in window:
                window.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            window.add(nums[right])
            current_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
                window.remove(nums[left])
                current_sum -= nums[left]
                left += 1

        return max_sum
