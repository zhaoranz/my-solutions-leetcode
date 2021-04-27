class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n %3 != 0 or n == 0:
            return True if n ==1 else False
        n /=3
        
        if n %3 == 0 and n/3==1:
            return True
        return self.isPowerOfThree(n)
      
      
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==3 or n == 1:
            return True 
        if n ==0: 
            return False
        while True:
            if n %3 !=0:
                return False
            n/=3
            if n ==3:
                return True
