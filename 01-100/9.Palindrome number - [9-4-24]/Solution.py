class Solution:
    def isPalindrome(self, x: int) -> bool:
        s1 = str(x)
        return s1 == s1[::-1]
