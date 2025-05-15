class Solution 
{
public:
    int maxArea(vector<int>& height) 
    {
        int max_area = 0, left = 0, right = height.size()-1;

        while(left < right)
        {
            int l = min(height[left], height[right]);
            int b = right - left;
            max_area = max(max_area, l*b);

            if(height[left] < height[right])
            {
                left++;
            }
            else
            {
                right--;
            }
        }

        return max_area;
    }
};
