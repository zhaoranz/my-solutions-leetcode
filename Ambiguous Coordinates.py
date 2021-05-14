class Solution:
    def subset(self,s:str):
        sb =[]
        for i in range(1, len(s)):
            if s[0]=='0' and i >1 : 
                continue
            if s[-1]=='0':
                continue
            sb.append(s[:i]+'.'+s[i:])
        if s=='0' or not s.startswith('0'):
            sb.append(s)
        return sb
    def ambiguousCoordinates(self, s: str) -> List[str]:

        s=s[1:-1]
        ans=[]
        for i in range(1, len(s)):
            x = self.subset(s[:i])
            y = self.subset(s[i:])
            for i in x:
                for j in y:
                    ans.append('('+i+', '+j+')')
        return ans
#solution-2
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag):
            N = len(frag)
            for d in range(1, N+1):
                left = frag[:d]
                right = frag[d:]
                if ((not left.startswith('0') or left == '0')
                        and (not right.endswith('0'))):
                    yield left + ('.' if d != N else '') + right

        s = s[1:-1]
        return ["({}, {})".format(*cand)
                for i in range(1, len(s))
                for cand in itertools.product(make(s[:i]), make(s[i:]))]
