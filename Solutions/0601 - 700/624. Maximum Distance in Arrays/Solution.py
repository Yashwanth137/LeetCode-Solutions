class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_d = 0
        
        for i in range(1, len(arrays)):
            max_d = max(max_d, abs(arrays[i][-1] - min_val))
            max_d = max(max_d, abs(max_val - arrays[i][0]))
        
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        
        return max_d
