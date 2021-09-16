class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[]
        if not matrix or len(matrix)==0:
            return result
        left, right=0, len(matrix[0])-1
        top, bottom=0, len(matrix)-1
        numEle=len(matrix) * len(matrix[0])
        while numEle>=1:
            i=left
            while i <=right and numEle>=1:
                result.append(matrix[top][i])
                i+=1
                numEle-=1
            top +=1
            
            i=top
            while i <=bottom and numEle>=1:
                result.append(matrix[i][right])
                i+=1
                numEle-=1
            right -=1
            
            i=right
            while i>=left and numEle>=1:
                result.append(matrix[bottom][i])
                i-=1
                numEle-=1
            bottom -=1
            i=bottom
            while i>=top and numEle>=1:
                result.append(matrix[i][left])
                i-=1
                numEle-=1
            left +=1
            
            
        
        return result
      
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        while matrix:
           # 削头（第一层）
            res+= matrix.pop(0)
             # 将剩下的逆时针转九十度，等待下次被削
            matrix=list(zip(*matrix))[::-1]       
        
        
        return res
        
        
