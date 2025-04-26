class CircularQueue:
    def __init__(self, k):
        self.size = k
        self.queue = [None] * k
        self.front = self.rear = -1

    def enqueue(self, value):
        # If queue is full
        if (self.rear + 1) % self.size == self.front:
            return False

        # First element being inserted
        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True

    def dequeue(self):
        if self.front == -1:
            return False

        # If single element
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def Front(self):
        if self.front == -1:
            return -1
        return self.queue[self.front]

    def Rear(self):
        if self.rear == -1:
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

# Usage
cq = CircularQueue(3)
print(cq.enqueue(1))  # True
print(cq.enqueue(2))  # True
print(cq.enqueue(3))  # True
print(cq.enqueue(4))  # False, queue is full
print(cq.Rear())      # 3
print(cq.isFull())    # True
cq.dequeue()
print(cq.enqueue(4))  # True
print(cq.Rear())      # 4
