class Solution:
    def totalNQueens(self, n: int) -> int:
        columns = set()
        diag1 = set()
        diag2 = set()
        def backtrack(row:int) -> int:
            if row == n:
                return 1
            else:
                count = 0
                for i in range(n):
                    if i in columns or row-i in diag1 or row+i in diag2:
                        continue
                    columns.add(i)
                    diag1.add(row-i)
                    diag2.add(row+i)
                    count += backtrack(row+1)
                    columns.remove(i)
                    diag1.remove(row-i)
                    diag2.remove(row+i)
                return count
        return backtrack(0)
            
