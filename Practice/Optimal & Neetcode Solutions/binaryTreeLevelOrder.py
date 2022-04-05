def levelOrder(self, root):
        
        if not root: return []
        
        queue = [root]
        values = []
        currentLevelValues = []
        
        while queue:
            
            levelLength = len(queue)
            
            i = 0
            
            for i in range(levelLength):
                node = queue.pop(0)
                currentLevelValues.append(node.val)
        
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            
            values.append(currentLevelValues)
            currentLevelValues = []
                
        return values