class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totalSum, negCount = 0,0
        smol_val = float('inf')

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                temp = matrix[i][j]
                totalSum += abs(temp)
                if temp < 0:
                    negCount += 1
                smol_val = min(smol_val, abs(temp))

        if negCount % 2 != 0:
            totalSum -= 2*smol_val
        
        return totalSum
