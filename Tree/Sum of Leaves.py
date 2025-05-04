class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        total = 0
        # If left child is a leaf, add its value
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        # Recur on left and right subtrees
        return total + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
