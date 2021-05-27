class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d= defaultdict(int)
        bit_n = lambda ch: ord(ch) - ord('a')
        
        for word in words:
            bitmask = 0
            for ch in word:
                bitmask = bitmask | (1 <<bit_n(ch))
            d[bitmask] = max(d[bitmask], len(word))
        max_prob = 0
        for x in d:
            for y in d:
                if x & y ==0:
                    max_prob = max(max_prob, d[x]*d[y])
        return max_prob
        
