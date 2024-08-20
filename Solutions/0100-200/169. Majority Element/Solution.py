class Solution(object):
    def majorityElement(self, nums):
        x=None
        for i in nums:
            if nums.count(i)>math.floor(len(nums)/2):
                return i
