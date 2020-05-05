class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.memo = {}
        count = self.helper(0, nums, 0, S)
        return count
    
    def helper(self, cur_sum, nums, index, S):
        if index == len(nums):
            if cur_sum == S:
                return 1
            return 0
        else:
            if index not in self.memo:
                self.memo[index] = {}
            if cur_sum not in self.memo[index]:
                minus = self.helper(cur_sum - nums[index], nums, index + 1, S)
                plus = self.helper(cur_sum + nums[index], nums, index + 1, S)
                self.memo[index][cur_sum] = minus + plus
                return minus + plus
            else:
                return self.memo[index][cur_sum]
