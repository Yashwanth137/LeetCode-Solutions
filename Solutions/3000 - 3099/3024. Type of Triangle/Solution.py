class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c = nums[0], nums[1], nums[2]

        if a+b <= c or b+c <= a or c+a <= b:
            return "none"

        if a == b and b == c:
            return "equilateral"
        
        elif a == b or b == c or c == a:
            return "isosceles"
        
        else:
            return "scalene"
