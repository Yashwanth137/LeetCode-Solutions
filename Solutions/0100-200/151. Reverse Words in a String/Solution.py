class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        s=s[::-1]
        s=" ".join(s)
        return s
