class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter()
        res = 0

        for i in nums:
            compliment = k - i
            if freq[compliment] > 0:
                res += 1
                freq[compliment] -= 1
            else:
                freq[i] += 1
        
        return res
