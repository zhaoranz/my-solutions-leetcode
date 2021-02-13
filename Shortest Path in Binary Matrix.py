class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not grid or grid[0][0] == 1 or grid[n-1][n-1]==1:
            return -1
        elif n<=2:
            return n
        path = [(0,0,1)]
        grid[0][0]=1
        
        while path:
            i, j, step = path.pop(0)
            for new_x, new_y in [(-1,-1), (1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1)]:
                    if i + new_x == n-1 and j + new_y == n-1:
                        return step + 1
                    if 0 <= new_x < n and 0 <= new_y < n and grid[i+new_x][j+new_y] == 0:
                        path.append((i+new_x, j+new_y, step + 1))
                        grid[i+new_x][j+new_y]=1

                
        return -1
