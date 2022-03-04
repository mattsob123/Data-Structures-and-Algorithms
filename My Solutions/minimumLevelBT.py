class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))


class Solution:
    def __init__(self):
        self.answer = None
    
    def traverse(self, node, currentDepth):

        currentDepth += 1

        if node.left:
            self.traverse(node.left, currentDepth)

        if node.right:
            self.traverse(node.right, currentDepth)

        if node.left == None and node.right == None:
            if self.answer == None:
                self.answer = currentDepth
            else:
                self.answer = min(self.answer, currentDepth)

    def minDepth(self, root):

        if root:
            self.traverse(root, 0)
        else:
            return 0

        return self.answer

minimum = Solution()

print(minimum.minDepth(tree))