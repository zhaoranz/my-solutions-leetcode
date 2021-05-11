class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        win_size = len(cardPoints) - k
        s = sum(cardPoints[:win_size])
        min_s = s
        for i in range(win_size, len(cardPoints)):
            s += cardPoints[i] - cardPoints[i-win_size]
            min_s = min(min_s, s)
        return total - min_s
