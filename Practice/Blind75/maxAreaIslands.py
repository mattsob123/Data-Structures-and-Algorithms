import collections


def maxAreaOfIsland(grid):
    
    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0
    maxSize = 0
        
    def bfs(r, c):
        q = collections.deque()
        visit.add((r,c))
        q.append((r,c))
        currentSize = 1
        while q:
            row, col = q.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and
                    c in range(cols) and 
                    grid[r][c] == "1" and (r,c) not in visit):
                    
                    q.append((r,c))
                    visit.add((r,c))
                    currentSize += 1
                    print(currentSize)
                        
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visit:
                bfs(r,c)
                print('eets')
                islands += 1
                
    return islands


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
maxAreaOfIsland(grid)