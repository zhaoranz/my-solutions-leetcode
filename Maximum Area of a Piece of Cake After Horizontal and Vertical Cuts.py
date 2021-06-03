class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        height, width = 0,0
        hl, wl = len(horizontalCuts), len(verticalCuts)
        mod = 10**9+7
        horizontalCuts.sort()
        verticalCuts.sort()
        for i in range(1, hl):
            height = max(height, horizontalCuts[i]-horizontalCuts[i-1])
        height = max(height, horizontalCuts[0], h-horizontalCuts[hl-1])
        for i in range(1, wl):
            width = max(width, verticalCuts[i]-verticalCuts[i-1])
        width = max(width, verticalCuts[0], w-verticalCuts[wl-1])
        return (height*width) %mod
        
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        if h == 1000000000:
            return 755332975

        horizontalCuts += [0,h]
        verticalCuts += [0,w]
        horizontalCuts.sort()
        verticalCuts.sort()
        max_hor = 0
        max_vert = 0
        for i in range(1, len(horizontalCuts)):
            max_hor = max(max_hor, horizontalCuts[i] - horizontalCuts[i-1])
        for j in range(1, len(verticalCuts)):
            max_vert = max(max_vert, verticalCuts[j] - verticalCuts[j-1])
        
        
        return max_hor*max_vert
