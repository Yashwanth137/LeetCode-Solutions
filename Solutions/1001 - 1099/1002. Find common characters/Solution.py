class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        for i in words:
            flag = Counter(i)
            for j in count.keys():
                count[j] = min(count[j], flag[j])
        res = []
        for i, j in count.items():
            res.extend([i] * j)
        return res
