class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        frequency = Counter({0: 1})
        result = current_odd_count = 0
        for num in nums:
            current_odd_count += num & 1
            result += frequency[current_odd_count - k]
            frequency[current_odd_count] += 1
        return result