class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        pos = 0
        n = len(spaces)

        for i in range(len(s)):
            if pos < n and i == spaces[pos]:
                res.append(" ")
                pos += 1
            res.append(s[i])
        
        return "".join(res)
