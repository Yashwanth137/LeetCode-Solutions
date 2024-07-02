class Solution(object):
    def islandPerimeter(self, grid):
        m,n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    if i < m-1 and grid[i+1][j] == 1:
                        res -= 2
                    if j < n-1 and grid[i][j+1] == 1:
                        res -= 2
        return res