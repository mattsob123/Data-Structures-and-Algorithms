def firstBadVersion(self, n: int) -> int:
    
    # g, g, g, g, g, g, b, b, b, b
    # want to find n where n = bad and n-1 = good
    
    left, right = 0, n
    
    while left <= right:
        
        index = (left + right) // 2
        
        if isBadVersion(index):
            if not isBadVersion(index-1):
                return index
            else:
                right = index - 1
        
        elif not isBadVersion(index):
            left = index + 1