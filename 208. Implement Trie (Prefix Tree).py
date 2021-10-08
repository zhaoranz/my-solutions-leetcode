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
        
class Trie:

    def __init__(self):
        """ Initialize your data structure here. """
        self.dic = {}

    def insert(self, word: str) -> None:
        """ Inserts a word into the trie. """
        cur = self.dic
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True

    def search(self, word: str) -> bool:
        """ Returns if the word is in the trie. """
        cur = self.dic
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '#' in cur

    def startsWith(self, prefix: str) -> bool:
        """ Returns if there is any word in the trie that starts with the given prefix. """
        cur = self.dic
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
