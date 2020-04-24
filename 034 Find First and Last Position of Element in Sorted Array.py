class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) == 0:
            return [-1, -1]
        first_index = self.first_occur(nums, target)
        if first_index == -1:
            return [-1, -1]
        else:
            end_index = first_index
            while end_index + 1 < len(nums) and nums[end_index + 1] == target:
                end_index += 1
            return [first_index, min(end_index, len(nums) - 1)]
    
    def first_occur(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
