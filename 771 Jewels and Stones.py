class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J_set = set(list(J))
        count = 0
        for s in S:
            if s in J_set:
                count += 1
        return count
