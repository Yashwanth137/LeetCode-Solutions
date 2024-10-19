class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = (1 << n) - 1  
        
        if n == 1:
            return "0"
        
        mid = (length // 2) + 1  
        
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n - 1, k)  
        else:
            new_k = length - k + 1  
            bit = self.findKthBit(n - 1, new_k)
            return "1" if bit == "0" else "0"
