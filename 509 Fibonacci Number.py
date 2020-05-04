class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        prev_prev = 0
        prev = 1
        curr = prev_prev + prev
        count = 2
        while count < N:
            prev_prev = prev
            prev = curr
            curr = prev_prev + prev
            count += 1
        return curr
