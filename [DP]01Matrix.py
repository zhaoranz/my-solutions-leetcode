class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r,c = len(mat),len(mat[0])
        dist =[[10**9]*c for _  in range(r)]
        for i in range(r):
            for j in range(c):
                if mat[i][j]==0:
                    dist[i][j]=0
        for i in range(r):
            for j in range(c):
                if i-1 >=0:
                    dist[i][j]=min(dist[i][j], dist[i-1][j]+1)
                if j-1>=0:
                    dist[i][j]=min(dist[i][j],dist[i][j-1]+1)
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                if i+1<r:
                    dist[i][j]=min(dist[i][j],dist[i+1][j]+1)
                if j+1<c:
                    dist[i][j]=min(dist[i][j],dist[i][j+1]+1)
        
                
        return dist
#BFS
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n=len(matrix), len(matrix[0])
        dirs=[(0,-1),(0,1),(1,0),(-1,0)]
        q=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    q.append((i,j))
                else:
                    matrix[i][j]=math.inf
        while q:
            x,y=q.pop(0)
            for direct in dirs:
                X,Y=x+direct[0], y+direct[1]
                if (X<0 or X>=m or Y<0 or Y>=n or matrix[X][Y]<=matrix[x][y]):
                    continue
                matrix[X][Y] = matrix[x][y]+1
                q.append((X,Y))
        return matrix
