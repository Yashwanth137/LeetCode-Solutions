class Solution:
    def numSteps(self, s: str) -> int:
        num, flag = int(s, 2), 0
        while(num != 1):
            if num % 2 == 1:
                num += 1
            else:
                num = num // 2
            flag += 1
        return flag
