from collections import deque

class Solution:
    def wallsAndGates(maze):
        iLen, jLen = len(maze), len(maze[0])
        EMPTY, WALL, GATE = 1e6, -1, 0 
        
        queue = deque()
        
        for i in range(iLen):
            for j in range(jLen):
                if maze[i][j] == GATE:
                    queue.append((i, j, 0))
        
        while queue: 
            i, j, d = queue.popleft()
        
            for i_off, j_off in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                new_i, new_j = i + i_off, j + j_off
                
                if 0 <= new_i < iLen and 0 <= new_j < jLen and maze[new_i][new_j] == EMPTY:
                    maze[new_i][new_j] = d + 1
                    queue.append((new_i, new_j, maze[new_i][new_j]))
        
maze = [[1e6, -1, 0, 1e6],
        [1e6, 1e6, 1e6, -1],
        [1e6, -1, 1e6, -1],
        [0, -1, 1e6, 1e6]]

solution = Solution()
Solution.wallsAndGates(maze)

print(maze)