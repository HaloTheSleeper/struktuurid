from collections import deque

class Solution:
    def wallsAndGates(maze):
        WALL, GATE, EMPTY = -1, 0, 1e6
        x, y = len(maze[0]), len(maze)
        
        queue = deque()
        
        for i in range(y):
            for j in range(x):
                if maze[i][j] == GATE:
                    queue.append((i, j, 0))
        
        while queue:
            i, j, d = queue.popleft()
            
            for i_off, j_off in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i, new_j = i + i_off, j + j_off
                
                if new_i >= 0 and new_i < y and new_j >= 0 and new_j < x and maze[new_i][new_j] == EMPTY:
                    maze[new_i][new_j] = d + 1
                    queue.append((new_i, new_j, maze[new_i][new_j]))
                    

maze = [[1e6, -1, 0, 1e6],
        [1e6, 1e6, 1e6, -1],
        [1e6, -1, 1e6, -1],
        [0, -1, 1e6, 1e6]]

solution = Solution()
Solution.wallsAndGates(maze)

print(maze)