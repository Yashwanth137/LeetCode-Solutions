class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = sorted(nums, key = lambda x: (freq[x], -x))
        return res
