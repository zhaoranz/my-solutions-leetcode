class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack =[]
        j = 0
        sl = list(s)
        for i in range(len(s)):
            sl[j]=s[i]
            
            if j == 0 or sl[j-1] != sl[j]:
                stack.append(1)
            else:
                a = stack.pop() + 1
                if a == k:
                    j = j - k
                else:
                    stack.append(a)
                    
            j += 1
        return ''.join(sl[:j])
#solution 2
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        remove = []
        ## Generating possible duplicates
        for ch in set(s):
            remove.append(ch*k)
            
        old,new = s,s
        while True:
            for candidate in remove:
                new = new.replace(candidate,"")
            if len(old) == len(new):
                break
            old = new        
        return old
