class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        left = 0

        max_queue = []
        min_queue = []

        for right in range(n):
            while max_queue and nums[max_queue[-1]] <= nums[right]:
                max_queue.pop()
            max_queue.append(right)

            while min_queue and nums[min_queue[-1]] >= nums[right]:
                min_queue.pop()
            min_queue.append(right)

            while nums[max_queue[0]] - nums[min_queue[0]] > 2:
                left += 1

                if max_queue[0] < left:
                    max_queue.pop(0)
                if min_queue[0] < left:
                    min_queue.pop(0)

            count += (right - left + 1)

        return count
