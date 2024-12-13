class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        score = 0
        min_heap = [(nums[i], i) for i in range(n)]
        heapq.heapify(min_heap)
        used = [False]*n

        while min_heap:
            val, indx = heapq.heappop(min_heap)
            if used[indx]:
                continue
            
            score += val
            used[indx] = True
            
            if indx > 0:
                used[indx - 1] = True
            if indx < n-1:
                used[indx + 1] = True
        
        return score




        
