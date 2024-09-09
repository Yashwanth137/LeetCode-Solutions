class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        current = head
        
        while current and top <= bottom and left <= right:
            for col in range(left, right + 1):
                if current:
                    matrix[top][col] = current.val
                    current = current.next
            top += 1
            
            for row in range(top, bottom + 1):
                if current:
                    matrix[row][right] = current.val
                    current = current.next
            right -= 1
            
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    if current:
                        matrix[bottom][col] = current.val
                        current = current.next
                bottom -= 1
            
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    if current:
                        matrix[row][left] = current.val
                        current = current.next
                left += 1
        
        return matrix        
