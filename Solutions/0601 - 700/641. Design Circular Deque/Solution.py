class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [0] * k
        self.front = 0  
        self.rear = 0   
        self.size = 0   
        self.capacity = k  

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False  
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False  
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False  
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False  
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1  
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1  
        return self.deque[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
