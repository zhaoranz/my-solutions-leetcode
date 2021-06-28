class Solution:
    def removeDuplicates(self, S: str) -> str:
        # generate 26 possible duplicates
        duplicates = {2 * ch for ch in ascii_lowercase}
        
        prev_length = -1
        while prev_length != len(S):
            prev_length = len(S)
            for d in duplicates:
                S = S.replace(d, '')
                
        return S
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack =[]
        for ch in s:
            if stack and stack[-1]==ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
        
