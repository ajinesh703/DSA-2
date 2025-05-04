class Solution:
    def invertTree(self, root):
        if root:
            # Swap the left and right children
            root.left, root.right = root.right, root.left
            # Recur on the children
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
