class Solution:
    def constructArray(self, n: int, k: int) -> List[int]: 
        if not n or not k:
            return []
        res=[1]
        flag = 1
        for i in range(k, 0, -1):
            if flag == 1:
                res.append(res[-1]+i)
            else: res.append(res[-1]-i)
            
            flag = -flag
        if k+2 <=n:
            res.extend([i for i in range(k+2,n+1)])
            
        return res
# Solution 2
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]: 
        if not n or not k:
            return []
        res =[i for i in range(1,n+1)]
        for i in range(k+1):
            res[i] =k+1-i//2 if i%2 else i//2+1
  
        return res
