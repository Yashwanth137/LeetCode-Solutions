class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        for num in permutations(digits, 3):
            if num[0] == 0:
                continue
            if num[2] % 2 != 0:
                continue
            val = num[0]*100+num[1]*10+num[2]
            res.add(val)
        
        return sorted(res)
