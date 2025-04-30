class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        nums = [str(i) for i in nums]
        res = 0
        for i in nums:
            if len(i) % 2 == 0:
                res += 1
        
        return res
