class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(counter):
            total = 0
            for char in counter:
                if counter[char] > 0:
                    counter[char] -= 1
                    total += 1 + backtrack(counter)  
                    counter[char] += 1
            return total
        
        return backtrack(Counter(tiles))
