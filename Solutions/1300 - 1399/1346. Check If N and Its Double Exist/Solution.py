class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        Double = set()
        for num in arr:
            if num*2 in Double or (num % 2==0 and num//2 in Double):
                return True
            Double.add(num)
        return False
