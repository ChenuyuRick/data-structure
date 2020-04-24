class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(num, record):
            if num in record:
                return False
            if num == 1:
                return True
            sum = 0
            for i in str(num):
                sum += int(i) ** 2
            record.add(num)
            return helper(sum, record)
        
        record = set()
        return helper(n, record)
        
