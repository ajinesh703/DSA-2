class Solution:
    def binaryTreePaths(self, root):
        paths = []

        def dfs(node, path):
            if node:
                # Add current node to the path
                path += str(node.val)
                # If it's a leaf, save the path
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    # Continue path with '->' and recurse
                    path += '->'
                    dfs(node.left, path)
                    dfs(node.right, path)

        dfs(root, '')
        return paths
