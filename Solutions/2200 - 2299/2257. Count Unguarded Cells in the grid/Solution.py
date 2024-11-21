class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        for g in guards:
            matrix[g[0]][g[1]] = 'G'
        
        for w in walls:
            matrix[w[0]][w[1]] = 'W'
        
        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        for g in guards:
            x,y = g
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                while 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != 'G' and matrix[nx][ny] != 'W':
                    matrix[nx][ny] = 'P'
                    nx += dx
                    ny += dy
        
        res = sum([1 for row in matrix for c in row if c == 0])
        return res
        
