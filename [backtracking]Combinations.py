class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, path=[],[]
        def backtracking(n,k,start, path, res):
            if len(path)==k:
                res.append(path.copy())
            for i in range(start, n+1):
                path.append(i)
                backtracking(n,k, i+1,path, res)
                path.pop()
        backtracking(n,k,1, path, res)
        return res
