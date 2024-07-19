class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_row = [(min(row), row.index(min(row))) for row in matrix]
        res = []

        for value, col in min_in_row:
            if all(value >= matrix[row][col] for row in range(len(matrix))):
                res.append(value)

        return res
