class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        time = 0
        fresh = 0
        
        q = collections.deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
            
        while q and fresh > 0:

            for i in range(len(q)):

                directions = [[-1,0], [1,0], [0,-1], [0,1]]

                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r >= 0 and c >= 0 and r < ROWS and c < COLS and grid[r][c] == 1 and (r,c)):
                        q.append((r,c))
                        grid[r][c] = 2
                        fresh -= 1
            time += 1
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return time if fresh == 0 else -1
    
                