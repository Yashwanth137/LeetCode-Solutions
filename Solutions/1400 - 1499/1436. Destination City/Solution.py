class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        res = set()
        for cityA, cityB in paths:
            res.add(cityA)

        for _, cityB in paths:
            if cityB not in res:
                return cityB
