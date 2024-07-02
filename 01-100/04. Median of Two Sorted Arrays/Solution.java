class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        int n=(nums1.length+nums2.length);
		int k=0,i=0,j=0,m1=0,m2=0;
		for(i=0,j=0;k<n/2;)
		{
			if(j<nums2.length && i<nums1.length)
			{
				if(nums1[i]>nums2[j])
				{
					m1=nums2[j];
					j++;
					k++;
				}
				else
				{
					m1=nums1[i];
					i++;
					k++;
				}
			}else
			{
				if(j<nums2.length)
                {
                    m1=nums2[j];
                    j++;
                    k++;
                }
				else
                {
					m1=nums1[i];
                    i++;
                    k++;
                }
			}
		}
		if(j<nums2.length && i<nums1.length)
		{
			if(nums1[i]>nums2[j])
				m2=nums2[j];
			else
				m2=nums1[i];
		}
		else{
			if(j<nums2.length)
				m2=nums2[j];
			else
				m2=nums1[i];
		}
		if(n%2==1)
			return (m2/1.0);
		else
			return ((m1+m2)/2.0);
    }
}
