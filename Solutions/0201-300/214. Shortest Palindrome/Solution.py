class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
          
        rev_s = s[::-1]
        
        for i in range(len(s)):
            if s[:len(s) - i] == rev_s[i:]:
                return rev_s[:i] + s 
        
        return ""
