class Solution:
    def findTheCity(
        self, n: int, e: List[List[int]], t: int
    ) -> int:
        def dijkstra(src: int) -> int:
            dist = [inf] * n
            dist[src] = 0
            vis = [False] * n
            for _ in range(n):
                k = -1
                for j in range(n):
                    if not vis[j] and (k == -1 or dist[k] > dist[j]):
                        k = j
                vis[k] = True
                for j in range(n):
                    if dist[k] + g[k][j] < dist[j]:
                        dist[j] = dist[k] + g[k][j]
            return sum(d <= t for d in dist)

        g = [[inf] * n for _ in range(n)]
        for f, to, w in e:
            g[f][to] = g[to][f] = w
        ans, min_cnt = n, inf
        for i in range(n - 1, -1, -1):
            cnt = dijkstra(i)
            if cnt < min_cnt:
                min_cnt, ans = cnt, i
        return ans
