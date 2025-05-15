class Solution {
    public int firstUniqChar(String s) {
        int n=s.length();
        int[] freq=new int[26];
        for(int i=0;i<n;i++){
            char ch=s.charAt(i);
            freq[ch-'a']++;
        }
        for(int i=0;i<n;i++){
            char ch=s.charAt(i);
            if(freq[ch-'a']==1){
                return i;
            }
        }
        return -1;
    }
}
