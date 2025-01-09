class Solution 
{
public:
    int triangleNumber(vector<int>& nums) 
    {
        int res = 0;
        sort(nums.begin(), nums.end());
        for(int i=nums.size()-1; i > 1; i--)
        {
            int pntr1 = 0, pntr2 = i-1;
            while(pntr1 < pntr2)
            {
                if(nums[pntr1] + nums[pntr2] > nums[i])
                {
                    res += pntr2 - pntr1;
                    pntr2--;
                }
                else
                {
                    pntr1++;
                }
            }
        }     
        return res;
    }
};
