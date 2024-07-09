class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time, wait = 0, 0
        res = wait
        for arrival, cook in customers:
            if time < arrival:
                time = arrival
            time += cook
            wait += time - arrival

        return wait/len(customers)
