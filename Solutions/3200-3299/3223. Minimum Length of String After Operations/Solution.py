class Solution:
    def minimumLength(self, s: str) -> int:
        counts = Counter(s)

        for ch, cnt in counts.items():
            curr = cnt

            while curr > 2:
                curr -= 2
            
            counts[ch] = curr
        
        return sum(list(counts.values()))
