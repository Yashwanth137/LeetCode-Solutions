class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        n = len(robot)
        m = len(factory)

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for pos, limit in factory:
            new_dp = dp[:]
            
            for i in range(n):
                distance = 0
                for j in range(i, min(i + limit, n)):
                    distance += abs(robot[j] - pos)
                    new_dp[j + 1] = min(new_dp[j + 1], dp[i] + distance)
            
            dp = new_dp

        return dp[n]
