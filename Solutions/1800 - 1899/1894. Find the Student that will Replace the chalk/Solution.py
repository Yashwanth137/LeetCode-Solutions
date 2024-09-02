class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k %= total_chalk
        
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]
