class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        return temp_s == temp_s[::-1]
