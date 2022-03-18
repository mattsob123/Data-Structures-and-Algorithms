# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.answer = 0
    
    def findMaxDepth(self, node, currentDepth):
        
        if node == None: return
        
        currentDepth += 1
        
        if node.left == None and node.right == None:
            self.answer = max(self.answer, currentDepth)
    
        
        if node.left:
            self.findMaxDepth(node.left, currentDepth)
            
        if node.right:
            self.findMaxDepth(node.right, currentDepth)

    
    def maxDepth(self, root):
        
        self.findMaxDepth(root, 0)
        return self.answer
        