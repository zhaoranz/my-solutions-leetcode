Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i,2*len(word)-1):
                    cur = cur[word[j%len(word)]]
                    cur[WEIGHT]=weight
                    
                    
        

    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        for c in suffix +'#'+prefix:
            if c not in cur:
                return -1
            cur = cur[c]
        return cur[WEIGHT]
