class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = {}
        answer = []
        for i in edges:
            res.setdefault(i[1], []).append(i[0])
        for i in range(n):
            nodes = set()
            next_node = [i]
            while next_node:
                curr = next_node.pop()
                if curr in res:
                    for prev in res[curr]:
                        if prev not in nodes:
                            nodes.add(prev)
                            next_node.append(prev)
            answer.append(sorted(list(nodes)))
                
        return answer
