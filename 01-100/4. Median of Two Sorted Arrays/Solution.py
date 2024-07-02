class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)

        n1, n2 = len(A), len(B)
        left, right = 0, n1

        while left <= right:
            partitionX = (left + right) // 2
            partitionY = (n1 + n2 + 1) // 2 - partitionX

            maxLeftX = A[partitionX - 1] if partitionX != 0 else float('-inf')
            minRightX = A[partitionX] if partitionX != n1 else float('inf')

            maxLeftY = B[partitionY - 1] if partitionY != 0 else float('-inf')
            minRightY = B[partitionY] if partitionY != n2 else float('inf')

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (n1 + n2) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                right = partitionX - 1
            else:
                left = partitionX + 1

        return 0.0

