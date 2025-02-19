class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        leftmost = root  # Start with the root level
        while leftmost.left:  # Traverse levels until the last
            head = leftmost
            while head:  # Traverse nodes in the current level
                head.left.next = head.right  # Connect left child to right
                if head.next:  # Connect right child to next node's left
                    head.right.next = head.next.left
                head = head.next  # Move to next node in the level
            leftmost = leftmost.left  # Move to next level
        return root
