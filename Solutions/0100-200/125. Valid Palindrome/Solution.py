class Solution(object):
    def isPalindrome(self, s):
        s=[i for i in s.lower() if i.islower() or i.isdigit()]
        return s==s[::-1]
