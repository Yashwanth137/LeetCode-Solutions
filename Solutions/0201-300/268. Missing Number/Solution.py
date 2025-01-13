class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        flag = 0
        for i in nums:
            if i != flag:
                return flag
            flag += 1
        return flag
