class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-x for x in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            max_val = -heapq.heappop(max_heap)
            sqr_root = floor(max_val ** 0.5)
            heapq.heappush(max_heap, -sqr_root)
        
        return -sum(max_heap)
