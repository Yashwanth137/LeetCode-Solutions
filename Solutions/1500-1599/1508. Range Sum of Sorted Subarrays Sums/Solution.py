class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        temp = []
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                temp.append(curr)
        temp.sort()
        res = sum(temp[left-1:right])
        return res%1000000007
