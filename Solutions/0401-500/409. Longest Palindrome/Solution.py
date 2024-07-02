class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        palindrome_length = 0
        has_odd = False
        
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        for count in char_count.values():
            if count % 2 == 0:
                palindrome_length += count
            else:
                palindrome_length += count - 1
                has_odd = True
        
        return palindrome_length + 1 if has_odd else palindrome_length
