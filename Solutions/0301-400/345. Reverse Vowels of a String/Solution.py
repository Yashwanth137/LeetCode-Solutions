class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s)-1

        while left < right:
            while left < right and s[left] not in vowel:
                left += 1
            while left < right and s[right] not in vowel:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return ''.join(s)
