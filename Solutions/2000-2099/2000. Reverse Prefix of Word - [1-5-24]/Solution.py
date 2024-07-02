class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        n = word.index(ch)
        res = word[:n+1]
        return res[::-1] + word[n+1:]
