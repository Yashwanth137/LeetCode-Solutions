class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_distance(mid):
            count = 0
            for i in range(len(nums)):
                count += bisect.bisect_right(nums, nums[i] + mid, lo=i) - i - 1
            return count

        nums.sort()
        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            if count_distance(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low
