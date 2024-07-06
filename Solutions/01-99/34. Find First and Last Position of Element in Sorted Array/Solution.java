class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] arr={-1,-1};
        
        if(nums.length==0)
            return arr;
            
        int low=0,high=nums.length-1,mid=-1;
        boolean found=false;
        while(low<=high)
        {
            mid=(low+high)/2;
            if(nums[mid]<target)
                low=mid+1;
            else if(nums[mid]>target)
                high=mid-1;
            else
            {
                found=true;
                break;
            }
        }
        if(!found)
            return arr;
        
        int first=mid,last=mid;
        int i=mid;
        while(i>=0 && nums[i]==target)
        {
            first=i;
            i-=1;
        }
        i=mid;
        while(i<nums.length && nums[i]==target)
        {
            last=i;
            i+=1;
        }
        arr[0]=first;
        arr[1]=last;
        return arr;
    }
}
