class Solution:
    def minKBitFlips(self, bits: List[int], flipSize: int) -> int:
        length = len(bits)
        diff = [0] * (length + 1)
        flips = current = 0
        for index, bit in enumerate(bits):
            current += diff[index]
            if bit % 2 == current % 2:
                if index + flipSize > length:
                    return -1
                diff[index] += 1
                diff[index + flipSize] -= 1
                current += 1
                flips += 1
        return flips