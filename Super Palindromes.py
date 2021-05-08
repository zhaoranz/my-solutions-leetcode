class Solution(object):
    def superpalindromesInRange(self, left, right): 
        L = int(left)
        R= int(right)
        MAGIC = 1000000

        def reverse(x):
            ans = 0
            while x:
                ans = 10 * ans + x % 10
                x //= 10
            return ans

        def is_palindrome(x):
            return x == reverse(x)

        cnt = 0

        
        for k in range(MAGIC):
            s = str(k)  
            t = s + s[-2::-1]  
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(v):
                cnt += 1

        
        for k in range(MAGIC):
            s = str(k)  
            t = s + s[::-1]  
            v = int(t) ** 2
            if v > R: break
            if v >= L and is_palindrome(v):
                cnt += 1

        return cnt

                
        
