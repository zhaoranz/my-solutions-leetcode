class Solution:
    def __init__(self):
        self.res=set()
    def findLongestWord(self, s: str, d: List[str]) -> str:
        ans=""
        for ss in d:
            if len(ans) > len(ss):
                continue
            if self.is_substring(ss, s):
                if len(ans) < len(ss):
                    ans = ss
                else:
                    ans = min(ans, ss)
        return ans
    @staticmethod
    def is_substring(x,y):
        j = 0
        for i in range(len(y)):
            if j < len(x) and x[j]==y[i]:
                j+=1
                
        return j ==len(x)
