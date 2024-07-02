class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) <= 3:
            return nums
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        res = [i for i in dict1 if dict1[i] == 1]
        return res
