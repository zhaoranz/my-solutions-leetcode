class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j, stack = 0, []
        for num in pushed:
            stack.append(num)
            while stack and j < len(pushed) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return not stack
        
