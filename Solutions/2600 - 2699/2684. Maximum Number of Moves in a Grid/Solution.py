class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        max_moves = 0

        def dfs(row, col):
            if col == n - 1:
                return 0
            if dp[row][col] != -1:
                return dp[row][col]
            
            moves = 0
            for drow in [-1, 0, 1]:
                new_row, new_col = row + drow, col + 1
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] > grid[row][col]:
                    moves = max(moves, 1 + dfs(new_row, new_col))

            dp[row][col] = moves
            return dp[row][col]

        for i in range(m):
            max_moves = max(max_moves, dfs(i, 0))
        
        return max_moves
