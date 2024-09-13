class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        res = []
        for l, r in queries:
            res.append(prefix_xor[r + 1] ^ prefix_xor[l])
        
        return res
