class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            return self.maximumGain(s[::-1], y, x)
        res = 0
        stack1, stack2 = [], []
        for c in s:
            if c != 'b':
                stack1.append(c)
            else:
                if stack1 and stack1[-1] == 'a':
                    stack1.pop()
                    res += x
                else:
                    stack1.append(c)
        while stack1:
            c = stack1.pop()
            if c != 'b':
                stack2.append(c)
            else:
                if stack2 and stack2[-1] == 'a':
                    stack2.pop()
                    res += y
                else:
                    stack2.append(c)
        return res
