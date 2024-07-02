class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(i: int):
            if i == n:
                ans.append(t[:])
                return
            for j in range(i, n):
                if res[i][j]:
                    t.append(s[i : j + 1])
                    dfs(j + 1)
                    t.pop()

        n = len(s)
        res = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                res[i][j] = s[i] == s[j] and res[i + 1][j - 1]
        ans = []
        t = []
        dfs(0)
        return ans
