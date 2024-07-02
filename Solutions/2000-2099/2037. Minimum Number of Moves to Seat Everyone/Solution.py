class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        seats.sort()
        res = 0
        for i,j in zip(seats, students):
            res += abs(i-j)
        return res
