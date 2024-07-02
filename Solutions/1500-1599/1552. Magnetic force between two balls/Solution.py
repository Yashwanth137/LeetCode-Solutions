class Solution:
    def maxDistance(self, positions: List[int], balls: int) -> int:
        def canPlaceBalls(minDist):
            last_position = positions[0]
            count = 1
            for current_position in positions[1:]:
                if current_position - last_position >= minDist:
                    last_position = current_position
                    count += 1
            return count >= balls

        positions.sort()
        low, high = 1, positions[-1]
        while low < high:
            mid = (low + high + 1) >> 1

            if canPlaceBalls(mid):
                low = mid
            else:
                high = mid - 1
        return low

