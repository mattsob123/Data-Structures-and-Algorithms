

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def merge(self, node1, node2):

        if node1 and node2:

            node = TreeNode()
            node.val = node1.val + node2.val
            node.left = self.merge(node1.left, node2.left)
            node.right = self.merge(node1.right, node2.right)

            return node

        elif node1:
            return node1
        elif node2:
            return node2

        else:
            return None

    def mergeTrees(self, root1, root2):
        newTree = self.merge(root1, root2)
        return newTree
