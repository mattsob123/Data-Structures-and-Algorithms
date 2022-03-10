class Solution:
    def construct2DArray(self, original, m, n):
        
        origLen = len(original)
        
        newArray = []
        
        if origLen % n == 0:
            
            i = 0
            row = 1
            
            while i < origLen:
                currentRow = []
                
                while i < row*n:
                    currentRow.append(original[i])
                    i += 1
                    
                newArray.append(currentRow)
                row += 1
                    
            if len(newArray) == m and len(newArray[0]) == n:
                return newArray
            else:
                return []
                
        else:
            return []