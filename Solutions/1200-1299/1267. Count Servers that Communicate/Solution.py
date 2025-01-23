class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        row_counts = [sum(row) for row in grid]
        col_counts = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        
        total_servers = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                    total_servers += 1
        
        return total_servers
