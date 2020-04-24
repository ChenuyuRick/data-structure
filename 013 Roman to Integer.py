class Solution:
    def romanToInt(self, s: str) -> int:
        transition_map = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        num = 0
        for i in range(len(s)):
            if i == len(s) -1:
                num = num + transition_map[s[i]]
            else :
                if transition_map[s[i]] < transition_map[s[i+1]]:
                    num = num - transition_map[s[i]]
                else :
                    num = num + transition_map[s[i]]
            
        return num
