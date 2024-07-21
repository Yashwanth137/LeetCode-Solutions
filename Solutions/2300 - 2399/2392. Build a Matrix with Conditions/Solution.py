class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def f(cond):
            temp = defaultdict(list)
            dump = [0] * (k + 1)
            for a, b in cond:
                temp[a].append(b)
                dump[b] += 1
            q = deque([i for i, v in enumerate(dump[1:], 1) if v == 0])
            res = []
            while q:
                for _ in range(len(q)):
                    i = q.popleft()
                    res.append(i)
                    for j in temp[i]:
                        dump[j] -= 1
                        if dump[j] == 0:
                            q.append(j)
            return None if len(res) != k else res

        row = f(rowConditions)
        col = f(colConditions)
        if row is None or col is None:
            return []
        res = [[0] * k for _ in range(k)]
        m = [0] * (k + 1)
        for i, v in enumerate(col):
            m[v] = i
        for i, v in enumerate(row):
            res[i][m[v]] = v
        return res
