class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        indices = {}

        for i, ch in enumerate(s):
            if ch not in indices:
                indices[ch] = i
            else:
                dist1 = i - indices[ch] - 1
                dist2 = distance[ord(ch) - ord('a')]
                if dist1 != dist2:
                    return False
        
        return True
