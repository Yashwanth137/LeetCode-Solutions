class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def dfs(i: int) -> None:
            nonlocal res
            if i >= len(nums):
                res += 1
                return
            dfs(i + 1)
            if cnt[nums[i] + k] == 0 and cnt[nums[i] - k] == 0:
                cnt[nums[i]] += 1
                dfs(i + 1)
                cnt[nums[i]] -= 1

        res = -1
        cnt = Counter()
        dfs(0)
        return res
