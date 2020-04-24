class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = 1
        prod_result = [1 for i in range(len(nums))]
        
        for i in range(len(nums)):
            prod_result[i] *= temp
            temp *= nums[i]
        
        temp = 1
        
        for i in range(len(nums) - 1, -1, -1):
            prod_result[i] *= temp
            temp *= nums[i]
        
        return prod_result
