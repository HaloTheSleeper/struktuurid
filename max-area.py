class Solution:
    def maxAreaOfIsland(self, grid):
        max_area = 0
        m, n = len(grid), len(grid[0])
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] and ((i, j) not in visited):
                    area = 0
                    stk = [(i, j)]
                    visited.add((i, j))
                    
                    while stk:
                        new_i, new_j = stk.pop()
                        area += 1
                        
                        for i_off, j_off in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            r, c = new_i + i_off, new_j + j_off
                            
                            if (0 <= r < m and 0 <= c < n) and grid[r][c] and (r, c) not in visited:
                                visited.add((r, c))
                                stk.append((r, c))
                    
                    max_area = max(area, max_area) 
        
        return max_area 
    
    
grid = [[0, 1, 0, 0, 1],
          [1, 1, 0, 1, 1],
          [1, 1, 0, 0, 0]]

areaClass = Solution()
print(areaClass.maxAreaOfIsland(grid))