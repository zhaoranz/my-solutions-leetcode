class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) %4 !=0:
            return False
        n = len(matchsticks)
        side = sum(matchsticks) //4
        matchsticks.sort(reverse=True)
        done=set()
        def dfs(i, need):
            if i == n:
                return False
            if i in done:
                return dfs(i+1, need)
            if matchsticks[i] == need:
                done.add(i)
                return True
            if matchsticks[i] < need:
                done.add(i)
                if dfs(i+1, need - matchsticks[i]):
                    return True
                done.remove(i)
                return dfs(i+1, need)
            return dfs(i+1, need)
        
        for _ in range(4): 
            if not dfs(0, side): 
                return False
        return True
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
            
        n=len(matchsticks)
        perimeter = sum(matchsticks)
        side = perimeter //4
        if side*4 != perimeter:
            return False
        matchsticks.sort(reverse=True)
        four =[0]*4
        
        def dfs(idx):
            if idx == n:
                return four[0]==four[1]==four[2]==side
            for i in range(4):
                if four[i]+matchsticks[idx] <= side:
                    four[i] += matchsticks[idx]
                    if dfs(idx+1):
                        return True
                    four[i] -= matchsticks[idx]
            return False
        return dfs(0)
                    
