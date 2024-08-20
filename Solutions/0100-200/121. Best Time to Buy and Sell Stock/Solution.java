class Solution {
    public int maxProfit(int[] prices) {
        int max=0;
        int n=prices.length;
        int buy=prices[0];
        for(int i=1;i<n;i++)
        {
            if(prices[i]>buy)
            {
                max=max>(prices[i]-buy)?max:(prices[i]-buy);
            }
            else
            {
                buy=prices[i];
            }
        }
        return max;
    }
}
