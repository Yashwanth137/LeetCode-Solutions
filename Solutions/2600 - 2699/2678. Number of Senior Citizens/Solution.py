class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for i in details:
            x = int(i[11:13])
            if x > 60:
                res += 1
        
        return res
