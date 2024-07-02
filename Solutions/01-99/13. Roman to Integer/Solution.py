class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        count=0
        while(i<len(s)):
            if (i+1)<len(s):
                if d[s[i]]<d[s[i+1]]:
                    count+=d[s[i+1]]-d[s[i]]
                    i=i+2
                else:
                    count+=d[s[i]]
                    i=i+1
            else:
                count+=d[s[i]]
                i=i+1
        return count
