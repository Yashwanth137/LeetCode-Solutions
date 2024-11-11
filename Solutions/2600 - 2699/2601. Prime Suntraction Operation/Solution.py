class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        max_num = max(nums)
        sieve = [True] * (max_num + 1)
        sieve[0], sieve[1] = False, False
        for i in range(2, int(max_num**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, max_num + 1, i):
                    sieve[j] = False
        p = [i for i, is_prime in enumerate(sieve) if is_prime]

        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                continue
            j = bisect_right(p, nums[i] - nums[i + 1])
            if j == len(p) or p[j] >= nums[i]:
                return False
            nums[i] -= p[j]
        return True
