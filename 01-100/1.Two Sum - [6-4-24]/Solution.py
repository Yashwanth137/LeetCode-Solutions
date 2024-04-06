class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        
        for i, num in enumerate(nums):
            b = target - num
            
            if b in res:
                return [res[b], i]
            
            res[num] = i
        
        return []
