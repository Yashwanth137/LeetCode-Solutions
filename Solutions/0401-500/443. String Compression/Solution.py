class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0

        while read < len(chars):
            ch = chars[read]
            count = 0

            while read < len(chars) and chars[read] == ch:
                count += 1
                read += 1
            
            chars[write] = ch
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
        return write
