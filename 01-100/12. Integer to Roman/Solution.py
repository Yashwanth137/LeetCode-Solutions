class Solution(object):
    def intToRoman(self, num):
        res=''
        dict={
            0:'', 1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'
        }
      
        d={}
        i=1000
        while(i>0):
            d[i]=num//i
            num=num%i
            i=i//10
         
        d=sorted(d.items(),reverse=True)
        
        for k,v in d:
            if 1<=v<=3:
                res+=dict[k]*v
            elif v==4:
                res+=dict[k]+dict[k*5]
            elif 5<=v<=8:
                res+=dict[5*k]+dict[k]*(v-5)
            elif v==9:
                res+=dict[k]+dict[k*10]
            else:
                res+=dict[0]
            
        return res
        
