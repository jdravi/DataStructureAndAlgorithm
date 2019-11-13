def tree_to_dll(self, root):
    if root is None:
        return
    else:
        self.tree_to_dll(root.left)
        if self.prev is None:
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root
        self.prev = root
        self.tree_to_dll(root.right)