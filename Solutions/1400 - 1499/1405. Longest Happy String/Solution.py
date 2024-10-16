class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = []
        counts = [['a', a], ['b', b], ['c', c]]
        
        while True:
            counts.sort(key=lambda x: -x[1])
            
            added = False
            
            for i in range(3):
                char, count = counts[i]
                if count == 0:
                    break
                
                if len(result) >= 2 and result[-1] == char and result[-2] == char:
                    continue
                
                result.append(char)
                counts[i][1] -= 1
                added = True
                break
            
            if not added:
                break
        
        return ''.join(result)
