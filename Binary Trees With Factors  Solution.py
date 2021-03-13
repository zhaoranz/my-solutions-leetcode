class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(arr)
        dp = [1] * N
        arr.sort()
        dict_i = {x:i for i, x in enumerate(arr)}
        for i,x in enumerate(arr):
            for j in range(i):
                if x % arr[j] ==0:
                    right = x/arr[j]
                    if right in dict_i:
                        dp[i] +=dp[j] * dp[dict_i[right]]
                        dp[i] %= MOD
        return sum(dp)%MOD
