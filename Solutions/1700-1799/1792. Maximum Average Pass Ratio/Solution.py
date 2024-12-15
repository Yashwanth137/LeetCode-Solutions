class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(x, y):
            return (x + 1) / (y + 1) - x / y

        max_heap = []
        for x, y in classes:
            heapq.heappush(max_heap, (-gain(x, y), x, y))
        
        for _ in range(extraStudents):
            neg_gain, x, y = heapq.heappop(max_heap)
            x, y = x + 1, y + 1
            heapq.heappush(max_heap, (-gain(x, y), x, y))
        
        total_ratio = 0
        while max_heap:
            _, x, y = heapq.heappop(max_heap)
            total_ratio += x / y
        
        return total_ratio / len(classes)
