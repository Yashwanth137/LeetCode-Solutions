class Solution:
    def first_missing_positive(self, numbers: List[int]) -> int:
        def swap(index1, index2):
            numbers[index1], numbers[index2] = numbers[index2], numbers[index1]

        size = len(numbers)
        for i in range(size):
            while 1 <= numbers[i] <= size and numbers[i] != numbers[numbers[i] - 1]:
                swap(i, numbers[i] - 1)
        for i in range(size):
            if i + 1 != numbers[i]:
                return i + 1
        return size + 1
