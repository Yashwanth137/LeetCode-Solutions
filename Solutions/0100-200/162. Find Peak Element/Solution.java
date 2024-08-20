class Solution {
    public int findPeakElement(int[] nums) {
        int start=0;
        int end=nums.length-1;
        int mid=0;

        while(start<=end)
        {
            mid=(start+end)/2;
            if((mid==0||nums[mid-1]<nums[mid])&&(mid==nums.length-1 || nums[mid]>nums[mid+1]))
            {
                break;
            }

            if(mid>0 && (nums[mid-1]>nums[mid]))
            {
                end=mid-1;
            }
            else
            {
                start=mid+1;
            }
        }
        return mid;
    }
}
