class Solution {
    public int maxArea(int[] height) {
        int start=0;
        int end=height.length-1;

        int vol=0;
        while(start<end)
        {
            int cal=(end-start)*Math.min(height[start],height[end]);
            if(cal>vol)
                vol=cal;
            if(height[start]<height[end])
                start+=1;
            else
                end-=1;
        }
        return vol;
    }
}
