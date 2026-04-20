
class Solution:
    def maxAreaOfIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] and ((i, j) not in visited):
                    stk = [(i, j)]
                    area = 0
                    visited.add((i, j))
                    
                    while stk:
                        new_i, new_j = stk.pop()
                        
                        area += 1
                        
                        for i_off, j_off in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            x, y = new_j + j_off, new_i + i_off
                            
                            if ((y, x) not in visited) and 0 <= y < m and 0 <= x < n and grid[y][x]:
                                stk.append((y, x))
                                visited.add((y, x))
                                
                    max_area = max(max_area, area)
        
        return max_area
                    
                    
grid = [[0, 1, 0, 0, 0],
          [1, 1, 0, 1, 1],
          [1, 1, 0, 0, 0]]

areaClass = Solution()
print(areaClass.maxAreaOfIsland(grid))