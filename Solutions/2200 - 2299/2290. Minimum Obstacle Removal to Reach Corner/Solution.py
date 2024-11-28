class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        qu = deque([(0, 0, 0)])
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while qu:
            i, j, k = qu.popleft()
            if i == m - 1 and j == n - 1:
                return k
            if (i, j) in visited:
                continue
            visited.add((i, j))

            for a, b in dirs:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    if grid[x][y] == 0:
                        qu.appendleft((x, y, k))
                    else:
                        qu.append((x, y, k + 1))

        return -1
