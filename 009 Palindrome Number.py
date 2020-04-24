class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        else :
            if int(str(abs(x))[::-1]) == x:
                return True
            else :
                return False
