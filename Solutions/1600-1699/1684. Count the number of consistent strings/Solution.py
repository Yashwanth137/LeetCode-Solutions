class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for word in words:
            flag = True 
            for letter in word:
                if letter not in allowed:
                    flag = False  
                    break  
            if flag:
                res += 1  
        return res
