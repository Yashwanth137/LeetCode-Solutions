class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < 2:
            return False
        prefix_sum = 0
        seen_mods = {0: -1}
        
        for i, num in enumerate(nums):
            prefix_sum += num
            if k != 0:
                prefix_sum %= k
            
            if prefix_sum in seen_mods:
                if i - seen_mods[prefix_sum] > 1:
                    return True
            else:
                seen_mods[prefix_sum] = i
        
        return False
