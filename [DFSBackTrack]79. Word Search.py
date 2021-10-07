class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs=[(0,1),(0,-1),(-1,0),(1,0)]
        m, n=len(board), len(board[0])
        visited=set()
        #it is also ok to use dfs(i,j,k)
        def dfs(board,visited,i, j, k):
            if board[i][j]!=word[k]:
                return False
            if k==len(word)-1:
                return True
            visited.add((i,j))
            res=False
            for d in dirs:
                ni, nj=i+d[0],j+d[1]
                if 0<=ni<len(board) and 0<=nj<len(board[0]):
                    if (ni,nj) not in visited:
                        if dfs(board,visited,ni,nj, k+1):
                            res=True
                            break
            visited.remove((i,j))
            return res
        for i in range(m):
            for j in range(n):
                if dfs(board,visited,i,j,0):
                    return True
        return False
      
      #dfs2
class Solution:
    dirs=[(0, 1), (0, -1), (1, 0), (-1, 0)]
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        if m==0:
            return False
        n=len(board[0])
        visited=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    visited[i][j]=1
                    if self.dfsBack(i,j,visited,board, word[1:])==True:
                        return True
                    else:
                        visited[i][j]=0
        return False
    def dfsBack(self, i,j,visited, board, word):
        if len(word)==0:
            return True
        for d in self.dirs:
            ni,nj=i+d[0],j+d[1]
            if 0<=ni<len(board) and 0<=nj<len(board[0]) and board[ni][nj]==word[0]:
                if visited[ni][nj]==1:
                    continue
                visited[ni][nj]=1
                if self.dfsBack(ni,nj, visited, board, word[1:])==True:
                    return True
                else:
                    visited[ni][nj]=0
        return False
                
                    
    
