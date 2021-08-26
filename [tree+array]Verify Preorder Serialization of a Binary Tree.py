class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if not preorder:
            return True
        stack=[]
        for node in preorder.split(','):
            while node=='#' and stack and stack[-1] =='#':
                stack.pop()
                if not stack:
                    return False
                stack.pop()
            stack.append(node)
        return stack==['#']
      
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slot = 1
        for node in preorder.split(','):
            slot -= 1
            if slot < 0:
                return False
            if node != "#":
                slot += 2
        return slot == 0
