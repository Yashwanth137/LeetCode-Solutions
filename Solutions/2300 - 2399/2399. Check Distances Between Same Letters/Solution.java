class Solution 
{
    public boolean checkDistances(String s, int[] distance) 
    {
        int[] indices = new int[26];
        Arrays.fill(indices, -1);

        for(int i=0; i<s.length(); i++)
        {
            char curr = s.charAt(i);
            int indx = curr - 'a';

            if(indices[indx] == -1)
            {
                indices[indx] = i;
            }
            else
            {
                int dist1 = i - indices[indx] - 1;
                if(dist1 != distance[indx])
                {
                    return false;
                }                
            }
        }
        return true;
    }
}
