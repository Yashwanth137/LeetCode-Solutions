class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = []

        for i in s:
            if i == ")":
                pos = []
                while res[-1] != "(":
                    pos.append(res.pop())
                res.pop()
                res.extend(pos)
            else:
                res.append(i)

        return "".join(res)
