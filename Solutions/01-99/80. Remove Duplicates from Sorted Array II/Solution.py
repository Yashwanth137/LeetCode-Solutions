class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        while(i!=len(nums)):
            if nums[:i+1].count(nums[i])>2:
                nums.pop(i)
            else:
                i+=1
        
