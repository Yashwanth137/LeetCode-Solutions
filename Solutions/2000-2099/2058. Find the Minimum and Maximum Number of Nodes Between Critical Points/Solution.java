class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        
        int[] arr={-1,-1};
        if(head.next.next==null)
            return arr;
        
        ListNode prev=head;
        ListNode current=head.next;
        
        int i=1;
        ArrayList<Integer> points=new ArrayList<Integer>();
        while(current.next!=null)
        {
            if(current.val<prev.val && current.val<current.next.val)
                points.add(i);
            else if(current.val>prev.val && current.val>current.next.val)
                points.add(i);
            i+=1;
            prev=current;
            current=current.next;
        }
        
        if(points.size()==0 || points.size()==1)
            return arr;
        else
        {
            int max=points.get(points.size()-1)-points.get(0);
            int min=max;
            for(int j=1;j<points.size();j++)
            {
                if((points.get(j)-points.get(j-1))<min)
                    min=points.get(j)-points.get(j-1);
                if(min==1)
                    break;
            }
            arr[0]=min;
            arr[1]=max;
        }
        return arr;
        
    }
}
