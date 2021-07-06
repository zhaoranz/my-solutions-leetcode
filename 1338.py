class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frek = collections.Counter(arr)
        ans, count =0,0
        for num, occ in frek.most_common():
            count += occ
            ans += 1
            if count *2 >= len(arr):
                break
        return ans
