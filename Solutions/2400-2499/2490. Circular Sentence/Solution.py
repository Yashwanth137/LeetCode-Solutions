class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        first_word = deque()
        last_word = deque()
        for i in sentence.split():
            first_word.append(i[0])
            last_word.append(i[-1])
        
        first_word.append(first_word.popleft())
        return first_word == last_word
