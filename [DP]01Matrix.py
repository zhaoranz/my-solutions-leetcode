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
        
