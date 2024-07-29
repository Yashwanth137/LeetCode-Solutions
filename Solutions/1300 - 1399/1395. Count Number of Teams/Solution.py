class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res, n = 0, len(rating)
        for i, b in enumerate(rating):
            l = sum(a < b for a in rating[:i])
            r = sum(c > b for c in rating[i + 1 :])
            res += l * r
            res += (i - l) * (n - i - 1 - r)
        return res
