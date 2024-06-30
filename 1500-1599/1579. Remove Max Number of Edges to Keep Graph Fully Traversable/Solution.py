class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))
        self.rank = [1] * size

    def find(self, u):
        if self.root[u] != u:
            self.root[u] = self.find(self.root[u])
        return self.root[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.root[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.root[rootU] = rootV
            else:
                self.root[rootV] = rootU
                self.rank[rootU] += 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufA = UnionFind(n + 1)
        ufB = UnionFind(n + 1)
        ufCommon = UnionFind(n + 1)
        
        totalEdges = 0
        
        for typei, u, v in edges:
            if typei == 3:
                if ufCommon.union(u, v):
                    ufA.union(u, v)
                    ufB.union(u, v)
                else:
                    totalEdges += 1

        for typei, u, v in edges:
            if typei == 1:
                if not ufA.union(u, v):
                    totalEdges += 1

        for typei, u, v in edges:
            if typei == 2:
                if not ufB.union(u, v):
                    totalEdges += 1
        
        if len(set(ufA.find(i) for i in range(1, n + 1))) != 1 or len(set(ufB.find(i) for i in range(1, n + 1))) != 1:
            return -1

        return totalEdges
