class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, n, right = 0, len(nums), k
        curr_sum, mean = 0, 0
        for i in range(0, k):
            curr_sum += nums[i]
        mean = curr_sum / k

        while right < n:
            curr_sum = curr_sum - nums[left] + nums[right]
            mean = max(mean, curr_sum / k)
            left += 1
            right += 1
        
        return mean
