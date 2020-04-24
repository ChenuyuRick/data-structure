class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count, dic, m = 0, {0:0}, 0
        for i, v in enumerate(nums):
            count += 2*v - 1
            if count in dic:
                m = max(m, i + 1 - dic[count])
            else:
                dic[count] = i + 1
        return m
