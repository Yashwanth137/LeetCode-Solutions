class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        current_max = float('-inf')
    
        for i, lst in enumerate(nums):
            heapq.heappush(heap, (lst[0], i, 0))
            current_max = max(current_max, lst[0])
    
        best_range = [float('-inf'), float('inf')]
    
        while heap:
            min_val, row, col = heapq.heappop(heap)
        
            if current_max - min_val < best_range[1] - best_range[0]:
                best_range = [min_val, current_max]
        
            if col + 1 < len(nums[row]):
                next_val = nums[row][col + 1]
                heapq.heappush(heap, (next_val, row, col + 1))
                current_max = max(current_max, next_val)
            else:
                break
        
        return best_range
