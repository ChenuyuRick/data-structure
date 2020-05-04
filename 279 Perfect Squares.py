class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 1:
            return n
        for i in range(n):
            if (i + 1) ** 2 > n:
                break
        least = i
        possible = [i**2 for i in range(1, least + 1)]
        
        queue = collections.deque([(0, 0)])
        seen = set()
        while queue:
            curr, nums = queue.popleft()
            if curr == n:
                return nums
            elif curr > n or curr in seen:
                continue
            else:
                seen.add(curr)
                for i in possible:
                    queue.append((curr + i, nums + 1))
        
