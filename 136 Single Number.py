class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # input: list, [int]
        # return: integer 
        a = 0
        for i in nums:
            a ^= i
        return a
