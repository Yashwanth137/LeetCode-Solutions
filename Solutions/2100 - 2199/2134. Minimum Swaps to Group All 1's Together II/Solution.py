class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        res = count = sum(nums[:k])
        n = len(nums)
        for i in range(k, n + k):
            count += nums[i % n]
            count -= nums[(i - k + n) % n]
            res = max(res, count)
        return k - res
