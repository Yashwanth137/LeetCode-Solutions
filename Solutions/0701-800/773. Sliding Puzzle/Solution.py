class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        adjcnt = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        bd = "".join([str(i) for row in board for i in row])
        target = "123450"
        zero_index = bd.index("0")
        qu = deque([(zero_index, bd, 0)])
        visited = set([bd])

        while qu:
            i, bd, length = qu.popleft()

            if bd == target:
                return length

            temp1 = list(bd)
            for j in adjcnt[i]:
                temp2 = temp1.copy()
                temp2[i], temp2[j] = temp1[j], temp1[i]
                val = "".join(temp2)
                if val not in visited:
                    qu.append((j, val, length + 1))
                    visited.add(val)
        
        return -1
