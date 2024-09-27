class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for overlap_start, overlap_end in self.overlaps:
            if max(start, overlap_start) < min(end, overlap_end):
                return False

        for booking_start, booking_end in self.bookings:
            overlap_start = max(start, booking_start)
            overlap_end = min(end, booking_end)
            if overlap_start < overlap_end:
                self.overlaps.append((overlap_start, overlap_end))

        self.bookings.append((start, end))
        return True
