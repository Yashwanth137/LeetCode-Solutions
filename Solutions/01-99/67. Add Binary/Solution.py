class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = int(a, 2)
        n2 = int(b, 2)
        res = n1 + n2
        return '{0:b}'.format(res)
