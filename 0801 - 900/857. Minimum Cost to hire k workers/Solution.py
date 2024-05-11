class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        list1 = sorted(zip(quality, wage), key=lambda x: x[1] / x[0])
        res, tot = inf, 0
        list2 = []
        for q, w in list1:
            tot += q
            heappush(list2, -q)
            if len(list2) == k:
                res = min(res, w / q * tot)
                tot += heappop(list2)
        return res
