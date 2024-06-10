class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected, res = sorted(heights), 0
        for i in range(0, len(heights)):
            if expected[i] != heights[i]:
                res += 1
        return res
