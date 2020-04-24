class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.clean(S) == self.clean(T)
    
    def clean(self, string):
        output = []
        for x in string:
            if x != '#':
                output.append(x)
            elif len(output) > 0:
                output.pop()
        return output
                
