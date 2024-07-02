class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        count = [0] * k
        count[0] = 1
        
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            res += count[prefix_sum]
            count[prefix_sum] += 1
        
        return res
