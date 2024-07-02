class Solution(object):
    def myAtoi(self, s):
        s=s.strip()
        match=re.search('^[-+]\d+|^\d+',s)
        if match!=None:
            x=match.group(0)
            while x!="" and x[0]=='0':
                x=x[1:]
            if x=="":
                return 0
            if int(x)>=pow(-2,31) and int(x)<=(pow(2,31)-1):
                return int(x)
            else:
                x=min(max(int(x),pow(-2,31)),pow(2,31)-1)
                return int(x)
        else:
            return 0
