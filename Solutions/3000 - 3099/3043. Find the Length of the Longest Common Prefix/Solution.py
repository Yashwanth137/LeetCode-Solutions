class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        str_arr1 = sorted([str(num) for num in arr1])
        str_arr2 = sorted([str(num) for num in arr2])
        
        i, j = 0, 0
        max_prefix = 0
        
        while i < len(str_arr1) and j < len(str_arr2):
            num1 = str_arr1[i]
            num2 = str_arr2[j]
            common_length = 0

            for k in range(min(len(num1), len(num2))):
                if num1[k] == num2[k]:
                    common_length += 1
                else:
                    break
            
            max_prefix = max(max_prefix, common_length)
            
            if num1 < num2:
                i += 1
            else:
                j += 1
        
        return max_prefix
