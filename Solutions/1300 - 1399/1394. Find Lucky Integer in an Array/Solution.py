class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        res = -1
        for k,v in freq.items():
            if k == v:
                res = max(res, v)
        
        return res
