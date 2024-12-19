class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_el = 0
        chunks = 0

        for i, num in enumerate(arr):
            max_el = max(max_el, num)
            if max_el == i:
                chunks += 1
        
        return chunks
