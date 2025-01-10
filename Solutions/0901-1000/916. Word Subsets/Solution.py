class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_count = Counter()
        for word in words2:
            word_count = Counter(word)
            for char in word_count:
                max_count[char] = max(max_count[char], word_count[char])
        
        res = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= max_count[char] for char in max_count):
                res.append(word)
        
        return res
