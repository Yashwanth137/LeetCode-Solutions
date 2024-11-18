class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n  

        if k == 0:
            return res  

        for i in range(n):
            if k > 0:
                res[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
            elif k < 0:
                res[i] = sum(code[(i + j) % n] for j in range(k, 0))

        return res
