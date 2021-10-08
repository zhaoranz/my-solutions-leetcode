# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Trie:

    def __init__(self):
        self.children=[None]*26
        self.isEnd=False
        
        

    def insert(self, word: str) -> None:
        node=self
        for ch in word:
            idx=ord(ch)-ord('a')
            if not node.children[idx]:
                node.children[idx]=Trie()
            node=node.children[idx]
        node.isEnd=True
            

    def search(self, word: str) -> bool:
        node=self
        for ch in word:
            idx=ord(ch)-ord('a')
            if not node.children[idx]:
                return False
            node=node.children[idx]
        return node.isEnd
   

    def startsWith(self, prefix: str) -> bool:
        node=self
        for ch in prefix:
            idx=ord(ch)-ord('a')
            if not node.children[idx]:
                return False
            node=node.children[idx]
        return node is not None
        
