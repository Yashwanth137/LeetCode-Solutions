class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        unq = Counter(freq.values())

        for k,v in unq.items():
            if v != 1:
                return False
            
        return True
