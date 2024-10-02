class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))
        rank_map = {num: rank + 1 for rank, num in enumerate(temp)}
        return [rank_map[num] for num in arr]
