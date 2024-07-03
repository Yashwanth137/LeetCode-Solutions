class Solution {
    public int minDifference(int[] nums) {
        if(nums.length<=4)
            return 0;
        
        Arrays.sort(nums);
        
        int res=nums[nums.length-1]-nums[0];
        for(int i=0;i<4;i++)
        {
            int right=nums.length-4+i;
            res=Math.min(res,nums[right]-nums[i]);
        }
        return res;
    }
}
