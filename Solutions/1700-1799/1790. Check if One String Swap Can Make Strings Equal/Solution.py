class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        diffs = [(a, b) for a, b in zip(s1, s2) if a != b]
        
        if not diffs:
            return True
        
        if len(diffs) == 2 and diffs[0] == diffs[1][::-1]:
            return True
        
        return False
