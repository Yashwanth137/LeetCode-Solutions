class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))  
        max_idx = {int(digit): i for i, digit in enumerate(num)}

        for i in range(len(num)):
            for d in range(9, int(num[i]), -1):
                if max_idx.get(d, -1) > i:
                    num[i], num[max_idx[d]] = num[max_idx[d]], num[i]
                    return int("".join(num))
        
        return int("".join(num)) 
