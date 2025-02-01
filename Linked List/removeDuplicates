def remove_duplicates(head):
    """Remove consecutive duplicates"""
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Usage:
ll = LinkedList()
ll.append(1)
ll.append(1)
ll.append(2)
remove_duplicates(ll.head)
ll.display()  # 1 -> 2 -> None
