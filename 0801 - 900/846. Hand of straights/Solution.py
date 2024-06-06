class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        for i in sorted(hand):
            if count[i]:
                for x in range(i, i + groupSize):
                    if count[x] == 0:
                        return False
                    count[x] -= 1
                    if count[x] == 0:
                        count.pop(x)
        return True
