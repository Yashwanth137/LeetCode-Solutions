class Solution(object):
    def reverse(self, x):
        num=0
        if x>=pow(-2,31) and x<=(pow(2,31)-1):
            str1=''
            if(x<0):
                str1+='-'
            x=str(abs(x))    
            for i in x[::-1]:
                str1+=i
            num=int(str1)
            if num>=pow(-2,31) and num<=pow(2,31)-1:
                return num
            else:
                return 0
        else:
            return 0
