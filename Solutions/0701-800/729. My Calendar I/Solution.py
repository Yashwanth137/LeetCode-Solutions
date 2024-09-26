class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.events:
            if max(start, s) < min(end, e):  
                return False  
                
        self.events.append((start, end))
        return True
