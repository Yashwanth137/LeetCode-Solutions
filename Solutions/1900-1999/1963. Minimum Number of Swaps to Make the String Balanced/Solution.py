class Solution:
    def minSwaps(self, s: str) -> int:
        imbalance = 0
        max_imbalance = 0
        
        for char in s:
            if char == '[':
                imbalance += 1
            else:  
                imbalance -= 1
            
            max_imbalance = min(max_imbalance, imbalance)
        
        return (-max_imbalance + 1) // 2
