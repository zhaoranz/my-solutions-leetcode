class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res= 0
        n = len(grid)
        heap =[(grid[0][0],0,0)]
        visited = set([(0,0)])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        
        while heap:
            height, x, y = heapq.heappop(heap)
            res = max(res, height)
            if x == n-1 and y == n-1:
                return res
            for dx, dy in directions:
                new_x, new_y = x+dx,y+dy
                if 0 <= new_x < n and 0<=new_y < n and (new_x,new_y) not in visited:
                    visited.add((new_x,new_y))
                    heapq.heappush(heap, (grid[new_x][new_y], new_x,new_y))
        return -1
      
 class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        l, r = grid[N - 1][N - 1], N * N - 1

        def is_reachable(t, loc):
            if loc == (N - 1, N - 1):
                return True
            i, j = loc
            if i < 0 or i > N - 1 or j < 0 or j > N - 1 or grid[i][j] > t or loc in seen:
                return False
            seen.add((i, j))
            return is_reachable(t, (i + 1, j)) or is_reachable(t, (i, j + 1)) or is_reachable(t, (
            i - 1, j)) or is_reachable(t, (i, j - 1))

        while l <= r:
            mid = (l + r) // 2
            seen = set()
            if is_reachable(mid, (0, 0)):
                r = mid - 1
            else:
                l = mid + 1
        return l
