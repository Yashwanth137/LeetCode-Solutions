class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        mask_to_index = {0: -1}
        mask = 0
        max_len = 0
        
        for i, char in enumerate(s):
            if char in vowels:
                mask ^= (1 << vowels[char])
            if mask in mask_to_index:
                max_len = max(max_len, i - mask_to_index[mask])
            else:
                mask_to_index[mask] = i
        
        return max_len
