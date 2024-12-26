def flatten(head):
    if not head:
        return head

    stack = []
    curr = head
    while curr:
        if curr.child:
            if curr.next:
                stack.append(curr.next)
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
        elif not curr.next and stack:
            temp = stack.pop()
            curr.next = temp
            temp.prev = curr
        curr = curr.next
    return head
