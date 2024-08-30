class Solution:
    def modifiedGraphEdges(
        self, n: int, edges: List[List[int]], source: int, destination: int, target: int
    ) -> List[List[int]]:
        def dijkstra(edges: List[List[int]]) -> int:
            g = [[] for _ in range(n)]
            for a, b, w in edges:
                if w != -1:
                    g[a].append((b, w))
                    g[b].append((a, w))
            dist = [float('inf')] * n
            dist[source] = 0
            min_heap = [(0, source)]  
            while min_heap:
                d, node = heapq.heappop(min_heap)
                if d > dist[node]:
                    continue
                for neighbor, weight in g[node]:
                    if d + weight < dist[neighbor]:
                        dist[neighbor] = d + weight
                        heapq.heappush(min_heap, (dist[neighbor], neighbor))
            return dist[destination]

        inf = 2 * 10**9
        d = dijkstra(edges)
        if d < target:
            return []
        ok = d == target
        for e in edges:
            if e[2] > 0:
                continue
            if ok:
                e[2] = inf
                continue
            e[2] = 1
            d = dijkstra(edges)
            if d <= target:
                ok = True
                e[2] += target - d
        return edges if ok else []
