class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = []
        n = len(score)
        res = {}
        scores = sorted(score, reverse=True)
        for i in range(n):
            if i == 0:
                res[scores[i]] = 'Gold Medal'
            elif i == 1:
                res[scores[i]] = 'Silver Medal'
            elif i == 2:
                res[scores[i]] = 'Bronze Medal'
            else:
                res[scores[i]] = str(i+1)
        
        for i in score:
            answer.append(res[i])

        return answer
