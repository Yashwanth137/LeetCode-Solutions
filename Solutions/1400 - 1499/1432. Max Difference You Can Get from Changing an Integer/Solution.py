class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        for i in num_str:
            if i != '9':
                a = int(num_str.replace(i, '9'))
                break
            else:
                a = num
        
        if num_str[0] != '1':
            b = int(num_str.replace(num_str[0], '1'))
        else:
            for i in num_str[1:]:
                if i != '1' and i != '0':
                    b = int(num_str.replace(i, '0'))
                    break
                else:
                    b = num

        return a - b
