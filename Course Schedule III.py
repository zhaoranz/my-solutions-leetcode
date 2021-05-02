class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        heap, count = [], 0
        for c in courses:
            if count + c[0] <= c[1]:
                heapq.heappush(heap, -1*c[0])
                count += c[0]
            elif heap:
                max_val = -1 * heapq.heappop(heap)
                heapq.heappush(heap, -1 * min(c[0], max_val))
                count = count -max_val + min(c[0], max_val)
        return len(heap)
