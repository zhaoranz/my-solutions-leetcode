class Solution:
    def calculate(self, s: str) -> int:
        digit, res, sign=0,0,1
        opt=('+','-')
        stack=[]
        for c in s:
            if c.isdigit():
                #deal with numbers with more than 1 digits
                digit = 10*digit+int(c)
            elif c in opt:
                res+=sign*digit
                digit=0
                sign=1 if c=='+' else -1
            elif c=='(':
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
            elif c==')':
                res += sign*digit
                digit=0
                res*=stack.pop()
                res+=stack.pop()
        res += sign * digit
                
        return res
    
