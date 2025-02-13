class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        heapify(nums)

        while len(nums) > 1 and nums[0] < k:
            a = heappop(nums)
            b = heappop(nums)
            temp = max(a,b) + 2 * min(a,b)
            heappush(nums, temp)
            res += 1
        
        return res
