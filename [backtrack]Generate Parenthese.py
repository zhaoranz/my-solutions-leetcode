class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        ans =[]
        def backtrack(s, l, r):
            if len(s) == 2*n:
                ans.append(s)
            else:
                if l < n:
                    backtrack(s+'(',l+1,r)
                if l > r:
                    backtrack(s+')',l,r+1)
        backtrack("",0,0)
        return ans
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        if n == 0:
            return [""]
        if n == 1:
            return ['()']
        for closure in range(n):
            for left in self.generateParenthesis(closure):
                for right in self.generateParenthesis(n-1-closure):
                    ans.append('('+left+')'+right)
        return ans
