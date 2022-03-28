def swap(self, node):
    if node.left: self.swap(node.left)
    if node.right: self.swap(node.right)

    temp = node.left
    node.left = node.right
    node.right = temp

def invertTree(self, root):
    if root: self.swap(root)
    return root