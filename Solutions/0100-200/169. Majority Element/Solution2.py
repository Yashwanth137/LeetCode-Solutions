class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)

        for num, cnt in counts.items():
            if cnt > len(nums) // 2:
                return num 
