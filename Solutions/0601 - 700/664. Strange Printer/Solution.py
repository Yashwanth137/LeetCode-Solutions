class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        res = [[inf] * n for _ in range(n)]
        
        for i in range(n):
            res[i][i] = 1  
        
        for length in range(2, n + 1):  
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    res[i][j] = res[i][j - 1]  
                else:
                    for k in range(i, j):
                        res[i][j] = min(res[i][j], res[i][k] + res[k + 1][j])
        
        return res[0][n - 1]
66
