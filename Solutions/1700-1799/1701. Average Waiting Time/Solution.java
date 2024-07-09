class Solution {
    public double averageWaitingTime(int[][] customers) {
        int k=0;
        double time=0;
        for(int i=0;i<customers.length;i++)
        {
            int startTime=customers[i][0];
            int serviceTime=customers[i][1];
            
            int serviceStart=Math.max(startTime,k);
            int serviceEnd=serviceStart+serviceTime;
                
            time+=(serviceEnd-startTime);
            k=serviceEnd;
        }
        return (time/customers.length);
    }
}
