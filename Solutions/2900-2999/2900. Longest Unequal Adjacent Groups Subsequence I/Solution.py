class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        res.append(words[0])

        for i in range(0, len(words)-1):
            if groups[i] != groups[i+1]:
                res.append(words[i+1])

        return res
