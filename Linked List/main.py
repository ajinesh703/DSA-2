class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node


class LinkedList:
    def __init__(self):
        self.head = None  # Head of the list

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the end of the list
            current = current.next
        current.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # New node points to the current head
        self.head = new_node

    def insert_after_value(self, value, data):
        current = self.head
        while current and current.data != value:
            current = current.next
        if current:  # If the value is found
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
        else:
            print(f"Value {value} not found in the list.")

    def delete_by_value(self, value):
        if not self.head:  # If the list is empty
            print("List is empty.")
            return
        if self.head.data == value:  # If the head is to be deleted
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if current.next:  # If the value was found
            current.next = current.next.next
        else:
            print(f"Value {value} not found in the list.")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the pointer
            prev = current  # Move prev one step forward
            current = next_node  # Move current one step forward
        self.head = prev

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps
        return slow.data if slow else None

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_beginning(5)
    ll.display()  # Output: 5 -> 10 -> 20 -> 30 -> None
    
    ll.insert_after_value(20, 25)
    ll.display()  # Output: 5 -> 10 -> 20 -> 25 -> 30 -> None
    
    ll.delete_by_value(10)
    ll.display()  # Output: 5 -> 20 -> 25 -> 30 -> None
    
    print("Middle Element:", ll.find_middle())  # Output: Middle Element: 25
    print("Length of List:", ll.get_length())  # Output: Length of List: 4
    
    ll.reverse()
    ll.display()  # Output: 30 -> 25 -> 20 -> 5 -> None
