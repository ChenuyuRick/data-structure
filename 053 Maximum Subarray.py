
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_record = nums[0]
        max_curr = nums[0]
        
        for i in range(1, len(nums)):
            max_curr = max(nums[i], nums[i] + max_curr)
            max_record = max(max_curr, max_record)
        
        return max_record
