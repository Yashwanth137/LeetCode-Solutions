class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_dict = defaultdict(int)
        for i in arr:
            count_dict[i] += 1
        res = [key for key, value in count_dict.items() if value == 1]
        if len(res) < k:
            return ""
        return res[k-1]
