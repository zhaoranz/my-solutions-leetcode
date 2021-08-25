class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <0:
            return False
        low, high = 0, int(sqrt(c))
        while low <= high:
            total = low*low+high*high
            if total == c:
                return True
            elif total < c:
                low +=1
            else:
                high -=1
                
        return False
        
