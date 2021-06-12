class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp =[startFuel]+[0]*len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in range(i,-1,-1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t]+capacity)
        for i, d in enumerate(dp):
            if d>=target:
                return i
        return -1
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # priority queue
        pq = []
        res = i = 0
        while startFuel < target:
            while i < len(stations) and stations[i][0] <= startFuel:
                # Min heap to Max heap ("-")
                heapq.heappush(pq, -stations[i][1])
                i += 1
            if not pq:
                return -1
            startFuel += -heapq.heappop(pq)
            res += 1
        return res
