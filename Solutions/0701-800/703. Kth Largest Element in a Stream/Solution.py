class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.res = []
        for x in nums:
            self.add(x)

    def add(self, val: int) -> int:
        heappush(self.res, val)
        if len(self.res) > self.k:
            heappop(self.res)
        return self.res[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
