class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> li=new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        for(int i=0;i<nums.length-2;i++)
        {
            if(i>0 &&nums[i-1]==nums[i])
                continue;
            int j=i+1;
            int k=nums.length-1;
            while(j<k)
            {
                int sum=nums[i]+nums[j]+nums[k];
                if(sum==0)
                {
                    li.add(Arrays.asList(nums[i],nums[j],nums[k]));
                    while(j<k && nums[j]==nums[j+1])
                    {
                        j+=1;
                    }
                    while(j<k && nums[k]==nums[k-1])
                    {
                        k=k-1;
                    }
                    j+=1;
                    k-=1;
                }
                else if(sum<0)
                {
                    j=j+1;
                }
                else
                {
                    k=k-1;
                }
            }
        }
        return li;
    }
}
