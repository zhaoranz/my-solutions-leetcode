class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map={}
    def insert(self, key: str, val: int) -> None:
        self.map[key]=val
    def sum(self, prefix: str) -> int:
        ans=0
        for key in self.map.keys():
            if key.find(prefix)==0:
                ans+=self.map[key]
        return ans
class TrieNode(object):
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum(object):
    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key, val):
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score
