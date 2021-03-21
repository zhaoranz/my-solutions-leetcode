class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        set0 = collections.Counter(str(N))
        
        return any( set0== collections.Counter(str(1 << i)) for i in range(31))
