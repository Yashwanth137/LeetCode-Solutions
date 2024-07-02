class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        ans = 0
        mx_profit = 0
        i = 0
        n = len(jobs)
        
        for w in worker:
            while i < n and jobs[i][0] <= w:
                mx_profit = max(mx_profit, jobs[i][1])
                i += 1
            ans += mx_profit
        
        return ans