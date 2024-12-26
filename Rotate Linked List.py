def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head

    # Find length and tail
    length, tail = 1, head
    while tail.next:
        tail = tail.next
        length += 1

    # Effective rotations
    k %= length
    if k == 0:
        return head

    # Find new head
    prev, new_head = None, head
    for _ in range(length - k):
        prev = new_head
        new_head = new_head.next
    prev.next = None
    tail.next = head

    return new_head
