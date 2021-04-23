class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s)<2:
            return 0
        prev = 0
        cur = 1
        ans = 0
        cur_ord = s[0]
        
        for c in s[1:]:
            if c == cur_ord:
                cur += 1
                if cur <=prev:
                    ans +=1
            else:
                cur_ord = c
                prev = cur
                cur = 1
                ans +=1
        return ans
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s)<2:
            return 0
        counts =[]
        res=0
        i=0
        while i < len(s):
            count = 0
            c=s[i]
            while i < len(s) and s[i]==c:
                i+=1
                count +=1
            counts.append(count)
            
        for i in range(1, len(counts)):
            res +=min(counts[i], counts[i-1])
        return res
        
