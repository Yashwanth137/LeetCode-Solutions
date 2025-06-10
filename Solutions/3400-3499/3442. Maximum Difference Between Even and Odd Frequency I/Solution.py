class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        res = sorted(freq.values())
        maxx, minn, = 0, float('inf')
        for i in res:
            if i % 2 == 0:
                minn = min(minn, i)
            else:
                maxx= max(maxx, i)
        
        return maxx - minn
