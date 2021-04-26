class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        q=[]
        sum_h = 0
        
        for i in range(1, n):
            delta_h = heights[i] - heights[i-1]
            if delta_h > 0:
                heapq.heappush(q, delta_h)
                if len(q) > ladders:
                    sum_h += heapq.heappop(q)
                if sum_h > bricks:
                    return i-1
        return n-1
