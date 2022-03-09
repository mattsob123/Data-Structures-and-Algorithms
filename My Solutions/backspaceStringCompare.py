class Solution:
    
    def parseString(self, string):
        
        stack = []
        
        for letter in string:
            if letter == "#":
                if stack != []:
                    stack.pop(-1)
                    
            else:
                stack.append(letter)
                
        return stack
                
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        return self.parseString(s) == self.parseString(t)


# could use pointers and increment backwards through string