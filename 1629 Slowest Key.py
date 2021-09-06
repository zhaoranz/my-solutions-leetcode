class Solution:
    def slowestKey(self, rel: List[int], key: str) -> str:
        ind=0
        max_diff=rel[0]
        for i in range(1, len(rel)):
            diff=rel[i]-rel[i-1]
            if diff>max_diff:
                max_diff=diff
                ind=i
            elif diff==max_diff:
                if key[i]>key[ind]:
                    ind=i
        return key[ind]

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n=len(releaseTimes)
        last, longest=releaseTimes[0],releaseTimes[0]
        ans = keysPressed[0]
        for i in range(1,n):
            last_time=releaseTimes[i] - last
            if last_time > longest:
                longest=last_time
                ans = keysPressed[i]
            elif last_time == longest:
                ans = max(ans, keysPressed[i])
            last = releaseTimes[i]
        return ans
        
