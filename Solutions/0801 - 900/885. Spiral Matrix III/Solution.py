class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [[rStart, cStart]]
        if rows * cols == 1:
            return res
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_index = 0
        steps = 1
        
        while len(res) < rows * cols:
            dr, dc = directions[direction_index]
            for _ in range(steps):
                rStart += dr
                cStart += dc
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
            if direction_index % 2 == 1: 
                steps += 1
            direction_index = (direction_index + 1) % 4
        
        return res
