class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, indx) for indx, num in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            temp, indx = heapq.heappop(heap)
            temp *= multiplier
            heapq.heappush(heap, (temp, indx))

        res = [0]*len(nums)
        for num, indx in heap:
            res[indx] = num

        return res
