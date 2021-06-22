class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        heads=[[] for _ in range(26)]
        
        for word in words:
            it = iter(word)
            heads[ord(next(it))-ord('a')].append(it)
                    
        for l in s:
            l_idx = ord(l) - ord('a')
            old_bucket = heads[l_idx]
            heads[l_idx] = []
            
                        
            while old_bucket:
                it = old_bucket.pop()
                succ = next(it,None)
                if succ:
                    heads[ord(succ)-ord('a')].append(it)
                else:
                    res += 1


                    
        return res
