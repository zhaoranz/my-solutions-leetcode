class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited ={0}
        count=0
        q =[0]
        
        while q:
            x= q.pop(0)
            count += 1
            for i in rooms[x]:
                if i not in visited:
                    visited.add(i)
                    q.append(i)
        return count == len(rooms)
