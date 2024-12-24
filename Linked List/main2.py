class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Insert at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at a specific position
    def insert_at_position(self, position, data):
        if position < 1:
            print("Invalid position! Position should be >= 1.")
            return
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 2):
            if not current:
                print("Position out of bounds!")
                return
            current = current.next
        new_node.next = current.next if current else None
        current.next = new_node if current else None

    # Delete node at a specific position
    def delete_at_position(self, position):
        if not self.head:
            print("List is empty!")
            return
        if position == 1:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(position - 2):
            if not current or not current.next:
                print("Position out of bounds!")
                return
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            print("Position out of bounds!")

    # Delete the entire list
    def delete_list(self):
        self.head = None
        print("The list has been deleted.")

    # Detect if a cycle is present in the list
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # Remove duplicates from a sorted list
    def remove_duplicates(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    # Merge two sorted linked lists
    @staticmethod
    def merge_sorted(list1, list2):
        dummy = Node(0)
        tail = dummy
        a, b = list1.head, list2.head
        while a and b:
            if a.data < b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a if a else b
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

    # Display the linked list
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
    ll.insert_at_position(3, 15)  # Insert 15 at position 3
    ll.display()  # Output: 5 -> 10 -> 15 -> 20 -> 30 -> None

    ll.delete_at_position(3)
    ll.display()  # Output: 5 -> 10 -> 20 -> 30 -> None

    ll.delete_list()
    ll.display()  # Output: None

    # Detect cycle
    ll2 = LinkedList()
    ll2.insert_at_end(1)
    ll2.insert_at_end(2)
    ll2.insert_at_end(3)
    ll2.head.next.next.next = ll2.head  # Create a cycle
    print("Has Cycle:", ll2.has_cycle())  # Output: Has Cycle: True

    # Remove duplicates from a sorted list
    ll3 = LinkedList()
    ll3.insert_at_end(1)
    ll3.insert_at_end(1)
    ll3.insert_at_end(2)
    ll3.insert_at_end(3)
    ll3.insert_at_end(3)
    ll3.remove_duplicates()
    ll3.display()  # Output: 1 -> 2 -> 3 -> None

    # Merge two sorted linked lists
    l1 = LinkedList()
    l2 = LinkedList()
    l1.insert_at_end(1)
    l1.insert_at_end(3)
    l1.insert_at_end(5)
    l2.insert_at_end(2)
    l2.insert_at_end(4)
    l2.insert_at_end(6)
    merged = LinkedList.merge_sorted(l1, l2)
    merged.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
