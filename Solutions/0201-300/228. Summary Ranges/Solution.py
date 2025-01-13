class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        res = []
        left = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if left == nums[i - 1]:
                    res.append(str(left))
                else:
                    res.append(f"{left}->{nums[i-1]}")
                
                left = nums[i]
        
        if left == nums[-1]:
            res.append(str(nums[-1]))
        else:
            res.append(f"{left}->{nums[-1]}")
        
        return res
