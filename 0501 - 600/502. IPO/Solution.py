class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= min(capital)  and w not in capital:
            return 0
        projects = list(zip(capital, profits))
        heapify(projects)
        max_heap = []

        for _ in range(k):
            while projects and projects[0][0] <= w:
                heappush(max_heap, -heappop(projects)[1])
            if not max_heap:
                break
            w -= heappop(max_heap)
        
        return w
