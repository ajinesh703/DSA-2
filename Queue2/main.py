class QueueUsingStacks:
    def __init__(self):
        # Initialize two stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        # Always push new element onto stack1
        self.stack1.append(x)

    def dequeue(self):
        # If both stacks are empty, queue is empty
        if not self.stack1 and not self.stack2:
            return "Queue is empty"
        
        # If stack2 is empty, move all elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Now pop from stack2 (which has elements in correct order)
        return self.stack2.pop()

    def peek(self):
        # Similar to dequeue but return the element without popping
        if not self.stack1 and not self.stack2:
            return "Queue is empty"

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def is_empty(self):
        # Queue is empty only if both stacks are empty
        return not self.stack1 and not self.stack2

# Usage example
q = QueueUsingStacks()
q.enqueue(1)   # Add 1
q.enqueue(2)   # Add 2
q.enqueue(3)   # Add 3
print(q.dequeue())  # Remove 1 (FIFO)
print(q.peek())     # See 2
print(q.is_empty()) # Queue still has elements
