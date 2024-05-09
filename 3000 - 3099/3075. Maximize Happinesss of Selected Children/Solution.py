class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        for i, x in enumerate(happiness[:k]):
            x -= i
            res += max(x, 0)
        return res
