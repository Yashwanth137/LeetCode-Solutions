class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ""
        for i in s:
            if i.islower():
                res +=str(ord(i) - ord('a') + 1) 
            else:
                res += str(ord(i) - ord('A') + 1)
        
        for _ in range(k):
            res = str(sum(int(digit) for digit in res))

        return int(res)
