class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        
        left_p, right_p = 0,0
        for i in s:
            if i == '(':
                left_p += 1
            elif left_p > 0:
                left_p -= 1
            else:
                right_p += 1
        
        return left_p + right_p
