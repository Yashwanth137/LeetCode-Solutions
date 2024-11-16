class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def issorted(arr):
            for i in range(0, len(arr)-1):
                if arr[i+1] - arr[i] != 1:
                    return False
            return True
        
        res = []
        for i in range(0, len(nums)-k+1):
            temp = nums[i:i+k]
            if(issorted(temp)):
                res.append(max(temp))
            else:
                res.append(-1)
        
        return res
