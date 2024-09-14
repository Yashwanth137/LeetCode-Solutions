class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_bit = max(nums)
        sub_len, curr_len = 0,0
        
        for i in nums:
            if i == max_bit:
                curr_len += 1
                sub_len = max(curr_len, sub_len)
            else:
                curr_len = 0
            
        return sub_len
