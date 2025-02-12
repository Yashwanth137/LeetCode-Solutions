class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def getSum(num):
            res = 0
            while num:
                res += num%10
                num //= 10
            return res
        
        num_map = {}
        for i in nums:
            digit_sum = getSum(i)
            if digit_sum not in num_map:
                num_map[digit_sum] = []
            num_map[digit_sum].append(i)
        
        res = -1
        for key in num_map:
            if(len(num_map[key]) > 1):
                num_list = num_map[key]
                num_list.sort(reverse=True)
                res = max(res, num_list[0] + num_list[1])
        
        return res
