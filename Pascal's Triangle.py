class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]
        res=[[1]]
        while len(res) < numRows:
            newRow =[a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)
        return res
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]
        res=[]
        for i in range(numRows):
            row=[]
            for j in range(0, i+1):
                if j==0 or j == i:
                    row.append(1)
                else:
                    row.append(res[i-1][j] + res[i-1][j-1])
            res.append(row)
        return res
        
