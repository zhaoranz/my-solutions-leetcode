from collections import defaultdict
class Trie:
    def __init__(self):
        self.children=defaultdict(Trie)
        self.word=None
        
    def insert(self, word):
        node=self
        for c in word:
            node=node.children[c]
        node.word=word
        
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie=Trie()
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        m, n=len(board), len(board[0])
        ans=[]
        for word in words:
            trie.insert(word)
        def dfs(cur, x, y):
            if board[x][y] not in cur.children:
                return
            ch=board[x][y]
            succ=cur.children[ch]
            if succ.word:
                ans.append(succ.word)
                succ.word=None
            if succ.children:
                board[x][y]='#'
                for d in dirs:
                    nx, ny=x+d[0],y+d[1]
                    if 0<=nx<m and 0<=ny<n:
                        dfs(succ, nx, ny)
                board[x][y]=ch
            if not succ.children:
                cur.children.pop(ch)
        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)
        return ans
