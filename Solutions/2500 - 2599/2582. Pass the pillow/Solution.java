class Solution {
    public int passThePillow(int n, int time) {
        int dir=1,N=1;
        for(int i=1;i<=time;i++)
        {
            if((dir==1 && N<n)||(dir==-1 && N>1))
                N=N+dir;
            else
            {
                dir=-dir;
                N=N+dir;
            }
        }
        return N;
    }
}
