from typing import List
from sortedcontainers import SortedList

class Solution:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        sorted_list = SortedList()
        max_length = start_index = 0
        for end_index, value in enumerate(arr):
            sorted_list.add(value)
            while sorted_list[-1] - sorted_list[0] > limit:
                sorted_list.remove(arr[start_index])
                start_index += 1
            max_length = max(max_length, end_index - start_index + 1)
        return max_length
