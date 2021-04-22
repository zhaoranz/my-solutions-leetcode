class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d= collections.defaultdict(int)
        for row in wall:
            total = 0
            for r in row[:-1]:
                total += r
                d[total]+= 1
        return len(wall) - max(d.values(), default=0)
        
