class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        o_d = {c:i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            if self.compare_false(words[i], words[i+1], o_d):
                return False
        return True
    def compare_false(self, x, y, o_d):
        for i in range(len(x)):
            if i >= len(y):
                return True
            if o_d[x[i]] > o_d[y[i]]:
                return True
            if o_d[x[i]] < o_d[y[i]]:
                return False
        return False
        
