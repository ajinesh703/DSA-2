class Solution:
    def minDepth(self, root):
        # If the tree is empty, depth is 0
        if not root:
            return 0
        # If left is None, recur on right
        if not root.left:
            return self.minDepth(root.right) + 1
        # If right is None, recur on left
        if not root.right:
            return self.minDepth(root.left) + 1
        # Take minimum of both subtrees
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
