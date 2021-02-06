class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        p = path.split("/")
        
        for i in p:
            if i =="..":
                stack.pop(y
            elif i and i!=".":
                stack.append(i)
        
        return "/" + "/".join(stack)
