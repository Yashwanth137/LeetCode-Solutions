class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        def find(day: int) -> bool:
            flag = 0
            temp = 0
            for i in bloomDay:
                flag = flag + 1 if i <= day else 0
                if flag == k:
                    flag = 0 
                    temp += 1 
            return temp >= m
        
        low, high = min(bloomDay), max(bloomDay)
        while low < high:
            mid = (low + high) >> 1
            if find(mid):
                high = mid
            else:
                low = mid + 1
        return low
                
