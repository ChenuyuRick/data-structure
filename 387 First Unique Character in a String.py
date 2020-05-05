class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
