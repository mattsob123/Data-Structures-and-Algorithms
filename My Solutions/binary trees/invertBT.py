# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverseInvert(self, newNode):
        temp = newNode.right
        newNode.right = newNode.left
        newNode.left = temp
        
        if newNode.left:
            self.traverseInvert(newNode.left)
            
        if newNode.right:
            self.traverseInvert(newNode.right)
    
    def invertTree(self, root):
        newRoot = root
        
        if newRoot:
            self.traverseInvert(newRoot)
            return newRoot
            
        else:
            return None
    