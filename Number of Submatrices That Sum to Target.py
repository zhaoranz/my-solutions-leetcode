class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row, col = len(matrix), len(matrix[0])
        presum = [[0 for _ in range(col+1)] for _ in range(row+1)]
        
        for r in range(row):
            for c in range(col):
                presum[r+1][c+1]=presum[r][c+1]+presum[r+1][c] - presum[r][c]+matrix[r][c]
        res = 0
        for r1 in range(row+1):
            for r2 in range(r1+1, row+1):
                dic = defaultdict(int)
                dic[0] = 1
                for c in range(1, col+1):
                    cursum=presum[r2][c] - presum[r1][c]
                    if cursum - target in dic:
                        res += dic[cursum - target]
                    dic[cursum] += 1
                    
        return res
