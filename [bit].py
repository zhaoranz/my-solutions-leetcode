#231. Power of Two

return n > 0 and bin(n).count('1') == 1

n > 0 and (n & -n) == n

#191. Number of 1 Bits
return bin(n).count('1')

class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res += 1
            n &=(n-1)
        
        return res
#190. Reverse Bits

