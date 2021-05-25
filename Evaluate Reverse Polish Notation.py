class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op ={
            '+': add,
            '-': sub,
            '*': mul,
            '/': lambda x,y : int(x/y)
        }
        
        stack =[]
        for token in tokens:
            try:
                n = int(token)
            except ValueError:
                n2 = stack.pop()
                n1= stack.pop()
                n = op[token](n1,n2)
            finally:
                stack.append(n)
            
        return stack[0]
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t in {"+", "-", "*", "/"}:
                r = s.pop()
                l = s.pop()
                if t == "+":
                    s.append(l + r)
                elif t == "-":
                    s.append(l - r)
                elif t == "*":
                    s.append(l * r)
                elif t == "/":
                    s.append(int(l / r))
            else:
                s.append(int(t))
        return s.pop()
