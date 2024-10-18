class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        n = len(nums)
        
        for num in nums:
            max_or |= num
        
        count = 0
        
        def dfs(i, current_or):
            nonlocal count
            if i == n:  
                if current_or == max_or:
                    count += 1
                return
            
            dfs(i + 1, current_or | nums[i]) 
            dfs(i + 1, current_or)  
        
        dfs(0, 0)
        
        return count
