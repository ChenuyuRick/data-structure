class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(': ')', '[':']', '{': '}'}
        for ch in s:
            if ch in dic:
                stack.append(ch)
            elif len(stack) > 0 and ch == dic[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
