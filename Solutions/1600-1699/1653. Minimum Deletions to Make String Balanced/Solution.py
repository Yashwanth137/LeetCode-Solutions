class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        res = [0] * (n + 1)
        b = 0
        for i, j in enumerate(s, 1):
            if j == 'b':
                res[i] = res[i - 1]
                b += 1
            else:
                res[i] = min(res[i - 1] + 1, b)
        return res[n]
