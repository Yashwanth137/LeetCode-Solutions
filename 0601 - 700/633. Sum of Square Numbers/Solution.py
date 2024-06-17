class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        temp = [i*i for i in range(int(c**0.5)+1)]
        low, high = 0, len(temp) - 1
     
        while low <= high:
            current_sum = temp[low] + temp[high]
            if current_sum > c:
                high -= 1
            elif current_sum < c:
                low += 1
            else:
                return True
        
        return False
