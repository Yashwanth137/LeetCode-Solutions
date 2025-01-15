class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = 0, 0

        for i in nums:
            if count == 0:
                candidate = i
                count = 1
            elif i == candidate:
                count += 1
            else:
                count -= 1
        
        count = 0
        for i in nums:
            if i == candidate:
                count += 1
        
        if count > len(nums)//2:
            return candidate
        
