class Solution:
    def __init__(self):
        self.combinations = []
    
    def letterCombinations(self, digits: str) -> List[str]:
        digit_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        if len(digits) == 0:
            return []
        
        if len(digits) == 1:
            return [digit_letters[char] for char in digits][0]
        
        self.combinations = digit_letters[digits[0]]
        
        for digit in digits[1:]:
            
            new_combinations = []
            print(new_combinations)
            
            for combination in self.combinations:
                
                for char in digit_letters[digit]:
                    new_combinations.append(combination + char)                    
            self.combinations = new_combinations
        
                
            
        
        return self.combinations
                            
     class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        q = ['']
        for digit in digits:
            
            for _ in range(len(q)):
                tmp = q.pop(0)
                for c in  phone[ord(digit)-50]:
                    q.append(tmp + c)
                    
        return q
                Letter Combinations of a Phone Number
