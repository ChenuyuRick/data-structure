class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        import collections
        dic = collections.defaultdict(int)
        result = 0
        accumulated_sum = 0
        dic[0] += 1
        for num in nums:
            accumulated_sum += num
            result += dic[accumulated_sum - k]
            dic[accumulated_sum] += 1
        return result
