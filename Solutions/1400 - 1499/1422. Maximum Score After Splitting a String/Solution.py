class Solution:
    def maxScore(self, s: str) -> int:
        left, right, score = 0, 0, 0
        for i in range(len(s)-1):
            left = s.count('0', 0, i+1)
            right = s.count('1', i+1, len(s))
            score = max(score, left + right)
        return score

            
