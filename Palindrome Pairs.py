class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        idx = {word[::-1]:i for i, word in enumerate(words)}
        res=[]
        def find_word(s:str, l:int, r:int) ->int:
            return idx.get(s[l:r+1],-1)
        def is_palindrome(s:str,l:int,r:int) ->bool:
            sub = s[l:r+1]
            return sub == sub[::-1]
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m+1):
                if is_palindrome(word, j, m-1):
                    left_id = find_word(word, 0, j-1)
                    if left_id != -1 and left_id != i:
                        res.append([i, left_id])
                if j and is_palindrome(word, 0, j-1):
                    right_id = find_word(word,j, m-1)
                    if right_id != -1 and right_id != i:
                        res.append([right_id,i])
        return res
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        #idx1 = {word:i for i, word in enumerate(words)}
        idx2 = {word[::-1]:i for i, word in enumerate(words)}
        res=[]
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                tmp1= word[:j]
                tmp2=word[j:]
                if tmp1 in idx2 and idx2[tmp1] != i and tmp2==tmp2[::-1]:
                    res.append([i, idx2[tmp1]])
                if j and tmp2 in idx2 and idx2[tmp2] !=i and tmp1==tmp1[::-1]:
                    res.append([idx2[tmp2],i])
        return res
        
