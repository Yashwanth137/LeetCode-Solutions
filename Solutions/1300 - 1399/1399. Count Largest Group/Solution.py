class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}
        max_size = 0

        for i in range(1, n+1):
            digit_sum = sum(map(int, str(i)))
            groups[digit_sum] = groups.get(digit_sum, 0) + 1
            max_size = max(max_size, groups[digit_sum])
        
        return sum(1 for size in groups.values() if size == max_size)
