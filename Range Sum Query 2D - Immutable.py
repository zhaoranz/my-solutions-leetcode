class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r, c = len(matrix), len(matrix[0]) if matrix else 0
        self.sums = [[0] *(c+1) for _ in range(r+1)]
        ans = self.sums
        for i in range(r):
            for j in range(c):
                ans[i+1][j+1] = ans[i][j+1] + ans[i+1][j]- ans[i][j] + matrix[i][j]
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.sums
        return res[row2+1][col2+1]-res[row1][col2+1]-res[row2+ 1][col1]+ res[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
