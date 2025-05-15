class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = -1   
        left, right = 0, len(height)-1

        while left < right:
            l = min(height[left], height[right])
            b = right - left
            max_area = max(max_area, l*b)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
