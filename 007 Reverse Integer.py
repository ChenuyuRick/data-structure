class Solution:
    def reverse(self, x: int) -> int:
        if x != 0  :
            answer = int(str(abs(x))[::-1])*int(abs(x)/x)
        else :
            answer = 0
            
        if answer>-2**31 and answer<2**31 :
            return answer
        else :
            return 0
        
