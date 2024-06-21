class Solution:
    def maxSatisfied(self, cus: List[int], gru: List[int], min: int) -> int:
        mx = cnt = sum(c * g for c, g in zip(cus[:min], gru[:min]))
        for i in range(min, len(cus)):
            cnt += cus[i] * gru[i]
            cnt -= cus[i - min] * gru[i - min]
            mx = max(mx, cnt)
        return sum(c * (g ^ 1) for c, g in zip(cus, gru)) + mx