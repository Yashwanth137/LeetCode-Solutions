class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()

        max_val = {}
        max_beauty = 0
        for price, beauty in items:
            max_beauty = max(max_beauty, beauty)
            max_val[price] = max_beauty

        sorted_prices = sorted(max_val.keys())
        max_beauties = [max_val[price] for price in sorted_prices]

        res = []
        for q in queries:
            idx = bisect_right(sorted_prices, q) - 1
            if idx >= 0:
                res.append(max_beauties[idx])
            else:
                res.append(0)

        return res
