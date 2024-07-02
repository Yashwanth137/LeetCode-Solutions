class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        res = {}
        max_sum = 0
        roads_list = [item for i in roads for item in i]
        vals = Counter(roads_list)
        dvals = sorted(vals.items(), key=lambda x:x[1], reverse=True)
        
        for i in range(0, len(dvals)):
            res[dvals[i][0]] = n-i

        for item in roads:
            temp_sum = 0
            for point in item:
                temp_sum += res[point]
            max_sum += temp_sum
        
        return max_sum
