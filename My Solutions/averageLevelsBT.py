# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverseLevels(self, queue, values):
        
        
        while queue:
            
            levelValues = []
            
            qLen = len(queue)
            
            for i in range(qLen):
                node = queue.pop(0)
                levelValues.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                
            values.append(levelValues)
            levelValues = []
            
    
    def calculateAverages(self, values, averages):
        
        for level in values:
            
            levelSum = 0
            levelCount = 0
            
            for number in range(len(level)):
                levelSum += level[number]
                levelCount += 1
            
            average = levelSum / levelCount
            averages.append(average)
            
        return averages
                
    
    def averageOfLevels(self, root):
        
        queue = []
        values = []
        averages = []
        
        if root:
            queue.append(root)
            self.traverseLevels(queue, values)
            averages = self.calculateAverages(values, averages)
            
        return averages
        
        
        