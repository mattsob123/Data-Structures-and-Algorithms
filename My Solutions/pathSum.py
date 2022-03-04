# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sumFound = False

    def traverse(self, node, currentSum, targetSum):
        if node.val:
            currentSum += node.val

        if node.left == None and node.right == None:
            if currentSum == targetSum:
                self.sumFound = True
            else:
                return

        else:
            if node.left:
                self.traverse(node.left, currentSum, targetSum)

            if node.right:
                self.traverse(node.right, currentSum, targetSum)

    def hasPathSum(self, root, targetSum):
        if root:
            self.traverse(root, 0, targetSum)

        return self.sumFound
