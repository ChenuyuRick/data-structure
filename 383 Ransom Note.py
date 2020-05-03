class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for c in magazine:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        for s in ransomNote:
            if s not in dic:
                return False
            else:
                dic[s] -= 1
                if dic[s] < 0:
                    return False
        return True
