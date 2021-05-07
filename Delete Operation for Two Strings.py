class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        l1, l2 = len(word1), len(word2)
        dp =[0]*(l2+1)
        for i in range(l1+1):
            temp = [0] *(l2+1)
            for j in range(l2+1):
                if i == 0 or j == 0:
                    temp[j]=i+j
                elif word1[i-1] == word2[j-1]:
                    temp[j] = dp[j-1]
                else:
                    temp[j] = 1 + min(temp[j-1], dp[j])
            dp = temp
        return dp[l2]
            
