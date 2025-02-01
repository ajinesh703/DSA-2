class Stack:
    """LIFO structure using linked list"""
    def __init__(self):
        self.head = None

    def push(self, data):
        """Add to top (head)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """Remove from top"""
        if not self.head:
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped

# Usage:
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # 20
