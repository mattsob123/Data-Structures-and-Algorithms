class Solution:
    """
    time O(n), space O(1)
    """
    def spiralOrder(self, matrix):

        tBound, lBound = 0, 0
        rBound, bBound = len(matrix[0]), len(matrix)
        px, py = lBound, tBound

        output = []

        while lBound < rBound and tBound < bBound:
            
            for i in range(lBound, rBound):
                output.append(matrix[tBound][i])
                
            tBound += 1
                
            for i in range(tBound, bBound):
                output.append(matrix[i][rBound-1])
                
            rBound -= 1
            
            if not (lBound < rBound and tBound < bBound):
                break
            
            for i in range(rBound-1, lBound-1, -1):
                output.append(matrix[bBound-1][i])
            
            bBound -= 1
                
            for i in range(bBound-1, tBound-1, -1):
                output.append(matrix[i][lBound])
                
            lBound += 1
            
        
        return output
        