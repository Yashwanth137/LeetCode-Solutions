class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(prefix, n):
            current = prefix
            next_prefix = prefix + 1
            steps = 0
            while current <= n:
                steps += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return steps
        
        curr = 1
        k -= 1  
        
        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1
        
        return curr
