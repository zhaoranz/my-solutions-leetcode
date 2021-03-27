class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        res=[]
        
        
        def count_word(word):
            ans=[0] *26
            for c in word:
                ans[ord(c)-ord('a')] +=1
            return ans
        bmax=[0]*26   
        for b in B:
            for i, c in enumerate(count_word(b)):
                bmax[i]=max(bmax[i], c)
        for a in A:
            if all(x>=y for x, y in zip(count_word(a), bmax)):
                res.append(a)
        return res
