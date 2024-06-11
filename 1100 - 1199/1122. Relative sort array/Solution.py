class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        temp = []
        for i in arr2:
            while i in arr1:
                temp.append(i)
                arr1.remove(i)
        for i in sorted(arr1):
            temp.append(i)
        return temp
