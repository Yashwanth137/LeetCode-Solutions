class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row, cols = len(rowSum), len(colSum)
        res = [[0] * cols for _ in range(row)]
        for i in range(row):
            for j in range(cols):
                val = min(rowSum[i], colSum[j])
                res[i][j] = val
                rowSum[i] -= val
                colSum[j] -= val
        return res
