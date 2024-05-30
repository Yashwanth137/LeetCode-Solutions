class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        l1 = [0] * (n + 1)
        for i in range(n):
            l1[i + 1] = l1[i] ^ arr[i]
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                for k in range(j, n):
                    a, b = l1[j] ^ l1[i], l1[k + 1] ^ l1[j]
                    if a == b:
                        res += 1
        return res
