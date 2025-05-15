class Solution 
{
    public int compress(char[] chars) 
    {
        int read = 0, write = 0;

        while(read < chars.length)
        {
            char ch = chars[read];
            int count = 0;

            while(read < chars.length && chars[read] == ch)
            {
                count++;
                read++;
            }

            chars[write] = ch;
            write++;

            if(count > 1)
            {
                for(char digit : String.valueOf(count).toCharArray())
                {
                    chars[write] = digit;
                    write++;
                }
            }
        }
        return write;
    }    
}
