class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        for i in range(len(gain)-1):
            gain[i+1] = gain[i] + gain[i+1]
        if max(gain) <= 0:
            return 0
        return max(gain)
