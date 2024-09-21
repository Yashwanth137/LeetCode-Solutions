class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [i for i in range(1,n+1)]        
        res = sorted(nums, key = lambda x:str(x))
        return res
