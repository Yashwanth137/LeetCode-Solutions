class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        ob = ['()','[]','{}']
        for b in s:
            if b in '([{':
                res.append(b)
            elif not res or res.pop() + b not in ob:
                return False
        return not res
