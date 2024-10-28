class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = set(nums)  
        max_streak = 0

        for num in sorted(num_set):  
            streak_length = 0
            current = num

            while current in num_set:
                streak_length += 1
                current = current * current
            
            max_streak = max(max_streak, streak_length)

        return max_streak if max_streak >= 2 else -1
