class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        res = 0
        for i, j in enumerate(sorted(count.values(), reverse=True)):
            res += (i // 8 + 1) * j
        return res
